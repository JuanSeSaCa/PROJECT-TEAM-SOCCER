import os
import json

federacion ={}
#Update a Agregar o Modificar infomacion en el diccionario
isAddTeam=True
while isAddTeam:
    os.system(('clear'))
    nombre=input("Ingrese el nombre del equipo: ")
    equipos={
        "nombre" : nombre,
        "PJ" :0 ,
        "PP":0,
        "PE" :0,
        "PG" :0,
        "GF" :0,
        "GC" :0,
        "PT":0
    }
    isAddTeam = bool(input("Desea continuar agregando mas equipos S(Si) o enter(No)"))
    print(equipos)
    federacion.update({str(len(federacion)).zfill(4):equipos})
print(json.dumps(federacion,indent=4))
