import datetime
fecha=datetime.datetime.now()
with open("servidor_minecraft/server.properties","r") as archivo:
    lineas = archivo.readlines()
    lineas_bak = lineas.copy()
    motd=lineas[27].split("2024")
    motd.pop(-1)
    motd.append(str(fecha.date())+"\n")
    new_motd = "".join(motd)
    lineas[27] = new_motd


with open("servidor_minecraft/server.properties", "w") as archivosi:
    archivosi.writelines(lineas)

with open("servidor_minecraft/server.propertiesbak", "w") as archivobak:
    archivobak.writelines(lineas_bak)