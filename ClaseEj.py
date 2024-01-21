import os
import json

federacion ={} #Update a Agregar o Modificar infomacion en el diccionario
campers=[]
grupos = {
    "A": [],
    "B": []
}

titulo=""""
    +++++++++++++++++++++++++++++
    + MENU OPCIONES OUG MONTIEL +
    +++++++++++++++++++++++++++++
"""

opciones="1. Aregar Equipo \n2. Hacer grupos\n3. tabla\n4. Salir" 
isActivate=True

while isActivate:
    
    os.system('clear')
    print(titulo)
    print(opciones)
    OP=int(input('>>'))
    
    if (OP==1):
        isAddTeam = True
        while isAddTeam:
            os.system('cls')
            nombre= input("Ingrese el nombre del equipo ")
            equipo={
                "nombre" : nombre,
                "pj":0,
                "pp":0,
                "pe":0,
                "pg":0,
                "gf":0,
                "gc":0,
                "estado":0
            }
            isAddTeam = bool(input("Desea continuar agregando mas equipos S(Si) o Enter(No)"))
            federacion.update({str(len(federacion)+1).zfill(4):equipo})
    if (OP==2):
        for key,valor in federacion.items():
            if valor["estado"]== 0:
                print("Seleccione el grupo al que quiere ingresar el equipo")
                for key2 in grupos:
                    if len(grupos[key2])<4:
                        print(f"{key2}. Grupo {key2}")
                    equipo={
                        "odEquipo": key,
                        "nombre":valor["nombre"]
                    }
                    grp=input(">>").upper()
                    grupos.get(grp).append(equipo)
                    federacion.get(key)["estado"]
    if (OP==4):
        isActive = False
    else :
        pass

print(json.dumps(federacion,indent=4))