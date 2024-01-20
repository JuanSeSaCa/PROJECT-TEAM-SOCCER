import os
os.system('clear')


Title="""
    +++++++++++++++++++++++++++++
    + PROJECT TEAM: OUG MONTIEL +
    +++++++++++++++++++++++++++++
"""
Option = "1. equipments registration\n2. data registration\n3. Tournament report\n4. go out"
isActivate=True
team=[]
# [id,nameTeam, PJ, PG, PP, PE, GF, GC, TP]
Matches=[]
# [time, home, visiting, goalhome,goalvisiting]]
####
while isActivate:
    os.system('clear')
    print(Title)
    print(Option)

    OP=int(input('>>'))
    if OP==1: #equipment registration
        id=str(len(team)).zfill(3)
        nameTeam=input("enter team name: ")
        PJ=0
        PG=0
        PP=0
        PE=0
        GF=0
        GC=0
        TP=0
        team.append([id,nameTeam,PJ,PG,PP,PE,GF,GC,TP])
    elif OP==2: #data registration
        time=int(input('enter time: '))
        isvalid=False;
        while isvalid==False:

            home=input("enter the team that will play at home: ") #Jugador local
            visitor=input("enter the team that will play as a visitor: ") #visitante

            goalhome=int(input(f"enter the home team's goals ({home}): "))
            goalvisitor=int(input(f"enter the visitor team's goals ({visitor}): "))

            Matches.append([time,home,visitor,goalhome,goalvisitor])

            print(Matches)
            print(team)

            for i,item in enumerate(team):
                if(item[1]== home):
                    temhome = i
                if(item[1]== visitor):
                    temvisitor = i

            print(temhome)
            print(temvisitor)

            if goalhome > goalvisitor: # [id,nameTeam, PJ, PG, PP, PE, GF, GC, TP]
                team[temhome][2] += 1
                team[temhome][3] += 1
                team[temhome][6] += goalhome
                team[temhome][7] += goalvisitor
                team[temhome][8] += 3

                team[temvisitor][2] += 1
                team[temvisitor][4] += 1
                team[temvisitor][6] += goalvisitor
                team[temvisitor][7] += goalhome

            elif goalvisitor > goalhome: # [id,nameTeam, PJ, PG, PP, PE, GF, GC, TP]
                team[temvisitor][2] += 1
                team[temvisitor][3] += 1
                team[temvisitor][6] += goalvisitor
                team[temvisitor][7] += goalhome
                team[temvisitor][8] += 3

                team[temhome][2] += 1
                team[temhome][4] += 1
                team[temhome][6] += goalhome
                team[temhome][7] += goalvisitor

            else : # [id,nameTeam, PJ, PG, PP, PE, GF, GC, TP]
                team[temhome][2] += 1
                team[temhome][5] += 1
                team[temhome][6] += goalvisitor
                team[temhome][7] += goalhome
                team[temhome][8] += 1

                team[temvisitor[2]] += 1
                team[temvisitor[5]] += 1
                team[temvisitor[6]] += goalhome
                team[temvisitor[7]] += goalvisitor
                team[temvisitor[8]] += 1

            isvalid=True

            # print('one of the teams already played this time')
            # print('enter a valid match')

        print(Matches)
        print(team)
    elif OP==3: #tournament report
        Tem=team[0][6]
        Equi=team[0][2]
        
        for i, item in enumerate(team):
            if item[6] >Tem:
                Tem=item[6]
                Equi=item[0]
        print(f"Nombre del equipo que mas goles anoto es: {Equi}")
               
        Tem=team[0][8]
        for i, item in enumerate(team):
            if item[8] >Tem:
                Tem=item[8]
                Equi=item[0]
        print(f"Nombre del equipo que mas puntos anoto es: {Equi} ")

        Tem=team[0][3]
        for i, item in enumerate(team):
            if item[3] >Tem:
                Tem=item[3]
                Equi=item[0]
        print(f"nombre del equipo que mas Partidos Gano es: {Equi}")
        
        
        Tem=0
        for i,item in enumerate(team):
                Tem += item[6]
        print(f"total de goles anotados por todos los equipos es: {Tem}")

        Tem= Tem/len(Matches)
        print(f"Promedio de goles anotados en el torneo es: {Tem}")
        isActivate=bool(input("Desea continuar agregando mas equipos S(Si) o enter(No)"))
    elif OP==4: #go out
        isActivate=False
    else:
        print("La opcion es erronea, intente de nuevo ")
        os.system('clear')

print(team)