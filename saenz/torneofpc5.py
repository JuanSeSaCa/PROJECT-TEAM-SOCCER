# # - NOMBRE DEL EQUIPO
#     - PJ,PG,PP,PE,GF,GC,TP
# REQUERIMIENTOS:
# 1. EL PROGRAMA DEBE PERMITIR REGISTRAR CADA UNO DE LOS EQUIPOS QUE VAN A
# PARTICIPAR EN EL TORNEO, TENGA EN CUENTA QUE AL MOMENTO DE REGISTRAR CADA
# EQUIPO LAS VARIABLES DE PJ,PG,PP,PE,GF,GC,TP DEBEN SER 0

# 2. REGISTRO DE FECHA. EL REGISTRO DE FECHAS SE DEBE INGRESAR LOS EQUIPOS
# QUE SE ENFRENTARON. EL PROGRAMA DEBE PERMITIR SELECCIONAR QUE EQUIPO JUGO DE
# LOCAL Y QUE EQUIPO JUGO DE VISITANTE. ADEMAS SE DEBE REGISTRAR EL MARCADOR DE
# CADA UNO DE LOS EQUIPOS. EL PROGRAMA DEBE DETERMINAR CUAL FUE EL EQUIPO
# GANADOR Y CUAL ES EL PERDEDOR Y ASIGNAR LOS VALORES CORRESPONDIENTES EN LA
# TABLA DE POSICIONES. RECUERDE QUE CADA PARTIDO GANADO EQUIVALE A 3 PUNTO
# Y LOS EMPATADOS EQUIVALEN A 1 PUNTO.

# 3. REPORTES
#     A. NOMBRE DEL EQUIPO QUE MAS GOLES ANOTO
#     B. NOMBRE DEL EQUIPO QUE MAS PUNTOS TIENE
#     C. NOMBRE DEL EQUIPO QUE MAS PARTIDOS GANO
#     D. TOTAL DE GOLES ANOTADOS POR TODOS LOS EQUIPOS
#     E. PROMEDIO DE GOLES ANOTADOS EN EL TORNEO
import os
os.system('cls')
titulo="""
    +++++++++++++++++++++++++++++++
    +  FFPC TORNEO APERTURA 2024  +
    +++++++++++++++++++++++++++++++
"""
#from tabulate import tabulate

opc="1. Registrar equipo \n2. Ingresar resultados \n3. Reportes \n4. Salir "
isActivate=True
teams=[]
nFecha=[]
tablaPos= []
i=1
while isActivate:
    os.system('cls') 
    print(titulo)
    print(opc)
    op=int(input("Ingrese la opcion que desea realizar: "))
    if(op==1):
        error1 = "si"
        while error1 == "si":
            os.system('cls')
            equipos = str(input(f'Ingrese el nombre del equipo a ingresar: (presiona S para salir): '))
            equipos = equipos.upper()
            if equipos == "S" :
               error1 = "no" 
            elif  equipos in teams:
                print('El equipo ya fue registrado, ingrese un nombre distinto')
            else:         
                #                 0  pj pg pp pe gf gc pts 
                  tablaPos.append([equipos,0,0,0,0,0,0,0])
                  teams.append(equipos)
                  i+=1
            for item in teams:
                    print(f'{item}')
                    error="no"         
            os.system('pause')
    elif(op==2):
        fechagame=int(input("Ingrese la fecha que se jugo: "))
        error1="s"
        while error1== "s":
           local=str(input(f'Ingrese el equipo local: '))
           local=local.upper()
           if local in teams: 
                error1="no"
           else:
                print('El equipo no esta registrado, ingrese un nombre distinto')
        error1 = "s"        
        while error1== "s":
           visita=str(input(f'Ingrese el equipo visitante: '))
           visita=visita.upper()
           if visita in teams: 
                error1="no"
           else:
                print('El equipo no esta registrado, ingrese un nombre distinto')
        #res1=(input'ingrese numero de goles que hizo el local'
        
        #res2=(input'ingrese numero de goles que hizo el local')
        gl=int(input(f'Ingrese los goles del {local} _ '))
        gv=int(input(f'Ingrese los goles del {visita} _ '))

        nFecha.append([fechagame, local, gl,visita, gv])
        for i in nFecha:
             print(i)
        os.system('pause')

        #                  0  pj pg pp pe gf gc pts 

        for j,item in enumerate(tablaPos):
              if(item[1]==local):
                    equipolocal =j
              if(item[1]==visita):
                    equipovisita =j
                    
        if gl>gv:
            print(f'el equipo ganador fue {local} que hizo {gl} goles, VS.{visita} que hizo {gv} goles')
                      
            tablaPos [equipolocal] [1] += 1
            tablaPos [equipolocal] [2] += 1
            tablaPos [equipolocal] [5] += gl
            tablaPos [equipolocal] [6] += gv
            tablaPos [equipolocal] [7] += 3

            tablaPos [equipovisita] [1] += 1
            tablaPos [equipovisita] [3] += 1
            tablaPos [equipovisita] [5] += gv
            tablaPos [equipovisita] [6] += gl
           
                    
                    
    #                 0  pj pg pp pe gf gc pts 
        elif gv>gl:
            
            print(f'el equipo ganador fue {visita} que hizo {gv} goles, VS.{local} que hizo {gl} goles')
            
            tablaPos [equipovisita] [1] += 1
            tablaPos [equipovisita] [2] += 1
            tablaPos [equipovisita] [5] += gv
            tablaPos [equipovisita] [6] += gl
            tablaPos [equipovisita] [7] += 3

            tablaPos [equipolocal] [1] += 1
            tablaPos [equipolocal] [2] += 1
            tablaPos [equipolocal] [5] += gl
            tablaPos [equipolocal] [6] += gv
            
    
    #                  0  pj pg pp pe gf gc pts 
        else:
            print(f'el resultado fue empate entre {local} que hizo {gl} goles, VS. {visita} que hizo {gv} goles')
            tablaPos [equipolocal] [1] += 1
            tablaPos [equipolocal] [4] += 1
            tablaPos [equipolocal] [5] += gl
            tablaPos [equipolocal] [6] += gv
            tablaPos [equipolocal] [7] += 1


            tablaPos [equipovisita] [1] += 1
            tablaPos [equipovisita] [4] += 1
            tablaPos [equipovisita] [5] += gv
            tablaPos [equipovisita] [6] += gl
            tablaPos [equipovisita] [7] += 1

#       #  isActivate=True
#    # elif (op==3):
                




#        # nEquip = str(input("Ingrese el numero del equipo a ingresar"))
#        # equipos.append([nEquip,0,0,0,0,0,0,0])
#         #print("Su equipo ha sido registrado con exito")
#        # os.system('pause')
        
    