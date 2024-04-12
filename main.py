from random import*
from time import*

#Поле игрока

Pole = [["▢"]*10 for i in range(10)]
#Pole = [[randint(0,9) for i in range(10)] for i in range(10)]
Koordinati = [[0]*11 for i in range(11)]
Koordinati2 = [i for i in range(11)]
Bykvi = [" ","А","Б","В","Г","Д","Е","Ж","З","И","К"]
Korabli = ["Линкор","Крейсер","Эсминец","Шлюпка"]
RazmerKorabl = [4,3,2,1]
KorabliIgroka = [[],[],[],[]]
KorabliIgroka2 = [[],[],[],[]]
KorabliKompa = [[],[],[],[]]
KorabliKompa2 = [[],[],[],[]]
KolKorabli = [1,2,3,4]
Os = ["x","y"]
for i in range(11):
    Koordinati[i][0]=i
    Koordinati[0][i]=Bykvi[i]
def VivodPola(Pola):
    for i in range(11):
        if(i<1):
            print(" ",end = "")
            for j in range(11):
                print(Koordinati[i][j],end = " ")
            print()
        else:
            print(Koordinati[i][0],end = " ")
            if(i<10):
                print(" ",end = "")
            for j in range(10):
                print(Pola[i-1][j],end = " ")
            print()
def VivodPolaBoy(Pola,Pola2):
    for i in range(11):
        if(i<1):
            print(" ",end = "")
            for j in range(11):
                print(Koordinati[i][j],end = " ")
            print("   ",end = "")
            for j in range(11):
                print(Koordinati[i][j],end = " ")
            print()
        else:
            print(Koordinati[i][0],end = " ")
            if(i<10):
                print(" ",end = "")
            for j in range(10):
                print(Pola[i-1][j],end = " ")
            print("  ",end = "")
            print(Koordinati[i][0],end = " ")
            if(i<10):
                print(" ",end = "")
            for j in range(10):
                print(Pola2[i-1][j],end = " ")
            print()
def ViborKorablei():
    ViborKor = input("Выберите корабль(Линкор,Крейсер,Эсминец,Шлюпка) ")
    if(ViborKor not in Korabli or KolKorabli[Korabli.index(ViborKor)] <= 0):
        print("Такого корабля нет")
        return(ViborKorablei())
    else:
        return(ViborKor)
def ViborOsi():
    ViborOs = input("Выберите ось корабля(x,y) ")
    if(ViborOs not in Os):
        print("Неправильно введена ось")
        return(ViborOsi())
    else:
        return(ViborOs)
def ViborMesto(Korabl,Osk):
    ViborKoordinti = input("Выберите место коробля(Корабли ставяться слева направо, и сверху вниз. Пример:А1) ")
    if(ViborKoordinti[1:] == "10"):
        Koor = [ViborKoordinti[:-2],ViborKoordinti[1:]]
    else:
        Koor = list(ViborKoordinti)
    G = 1
    F1 = 2
    F2 = 2
    if(Koor[0] not in Bykvi or int(Koor[1])>10):
        print("Неправильно введены координаты")
        return(ViborMesto(Korabl,Osk))
    else:
        B = int(Koor[1])+RazmerKorabl[Korabli.index(Korabl)]
        B2 = Bykvi.index(Koor[0])+RazmerKorabl[Korabli.index(Korabl)]
        if(Osk == 'x' and B2<=10):
            if(int(Koor[1])-F1 < 0 or int(Koor[1])+1 >= 10):
                F1=1
            else:
                F1=2
            if(Bykvi.index(Koor[0])-F2 < 0 or Bykvi.index(Koor[0]) >= 10):
                F2=1
            else:
                F2=2
            for x in range(0,RazmerKorabl[Korabli.index(Korabl)]):
                for i in range(int(Koor[1])-F1,int(Koor[1])+(F1-1)):
                    for j in range((Bykvi.index(Koor[0])-F2)+x,(Bykvi.index(Koor[0])+(F2-1))+x):
                        #print(Pole[i][j])
                        if(Pole[i][j] == "▩"):
                            G = 0
        if(Osk == 'y' and B<=10):
            if(int(Koor[1])-F1 < 0 or int(Koor[1])+1 >= 10):
                F1=1
            else:
                F1=2
            if(Bykvi.index(Koor[0])-F2 < 0 or Bykvi.index(Koor[0]) >= 10):
                F2=1
            else:
                F2=2
            for x in range(0,RazmerKorabl[Korabli.index(Korabl)]):
                for i in range((int(Koor[1])-F1)+x,(int(Koor[1])+(F1-1))+x):
                    for j in range(Bykvi.index(Koor[0])-F2,Bykvi.index(Koor[0])+(F2-1)):
                        #print(Pole[i][j])
                        if(Pole[i][j] == "▩"):
                            G = 0
        if(Osk == 'x' and B2<=10 and G == 1):
            Koor[0]=Koordinati[Bykvi.index(Koor[0])][0]
            return(Koor)
        else:
            if(Osk == 'y' and B<=10 and G == 1):
                Koor[0]=Koordinati[Bykvi.index(Koor[0])][0]
                return(Koor)
            else:
                print("Корабль не помещается")
                return(ViborMesto(Korabl,Osk))
def Postavit():
    VivodPola(Pole)
    print("Расположите свои корабли. У вас:\nЛинкоры(4кл) -",KolKorabli[0],"\nКрейсера(3кл) -",KolKorabli[1],"\nЭсминцы(2кл) -",KolKorabli[2],"\nШлюпки(1кл) -",KolKorabli[3])
    ViborKor = ViborKorablei()
    if(ViborKor!="Шлюпка"):
        ViborOs = ViborOsi()
    else:
        ViborOs = 'x'
    Koor = ViborMesto(ViborKor,ViborOs)
    if(ViborOs == 'x'):
        for i in range(Koor[0]-1,(Koor[0]-1)+RazmerKorabl[Korabli.index(ViborKor)]):
            Pole[int(Koor[1])-1][i] = "▩"
    if(ViborOs == 'y'):
        for i in range(int(Koor[1])-1,(int(Koor[1])-1)+RazmerKorabl[Korabli.index(ViborKor)]):
            Pole[i][int(Koor[0])-1] = "▩"
    KolKorabli[Korabli.index(ViborKor)] -= 1
    if((KolKorabli[0]+KolKorabli[1]+KolKorabli[2]+KolKorabli[3])>0):
        Postavit()
#Поле компьютера

Pole2 = [["▢"]*10 for i in range(10)]
KolKorabli2 = [1,2,3,4]
def ViborMesto2(Korabl,Osk,Pole2):
    r = 1
    while(r >= 1):
        Koor = [randint(0,9), randint(0,9)]
        GU = 1
        F1 = 1
        F2 = 1
        F22 = 1
        B = Koor[1]+RazmerKorabl[Korabl]
        B2 = Koor[0]+RazmerKorabl[Korabl]
        if(Osk == 0 and B2<=9):
            if(Koor[1]-F1 < 0):
                F1=0
            else:
                F1=1
            if(Koor[1]+1 >= 10):
                F11=0
            else:
                F11=1
            if(Koor[0]-F2 < 0):
                F2=0
            else:
                F2=1
            if(Koor[0]+1 >= 10):
                F22=0
            else:
                F22=1
            for x in range(0,RazmerKorabl[Korabl]):
                for i in range(Koor[1]-F1,Koor[1]+F11+1):
                    for j in range(Koor[0]-F2+x,(Koor[0]+F22)+x+1):
                        if(Pole2[i][j] == "▩"):
                            GU = 0
        if(Osk == 1 and B<=9):
            if(Koor[1]-F1 < 0):
                F1=0
            else:
                F1=1
            if(Koor[1]+1 >= 10):
                F11=0
            else:
                F11=1
            if(Koor[0]-F2 < 0):
                F2=0
            else:
                F2=1
            if(Koor[0]+1 >= 10):
                F22=0
            else:
                F22=1
            for x in range(0,RazmerKorabl[Korabl]):
                for i in range((Koor[1]-F1)+x,(Koor[1]+F11)+x+1):
                    for j in range(Koor[0]-F2,Koor[0]+F22+1):
                        if(Pole2[i][j] == "▩"):
                            GU = 0
        if(Osk == 0 and B2<=9 and GU == 1):
            Koor[0]=Koordinati[Koor[0]][0]
            r = 0
            return(Koor)
        else:
            if(Osk == 1 and B<=9 and GU == 1):
                Koor[0]=Koordinati[Koor[0]][0]
                r = 0
                return(Koor)
def Postavit2(b,Pole2,n):
    ViborOs = randint(0,1)
    Koor = ViborMesto2(b,ViborOs,Pole2)
    Kora = []
    for i in range(1):
        if(Koor[i]==' '):
            Koor[i]=0
    if(ViborOs == 0):
        for i in range(Koor[0],Koor[0]+RazmerKorabl[b]):
            Pole2[Koor[1]][i] = "▩"
            K = [Koor[1],i]
            Kora += [K]
    if(ViborOs == 1):
        for i in range(Koor[1],Koor[1]+RazmerKorabl[b]):
            Pole2[i][Koor[0]] = "▩"
            K = [i,Koor[0]]
            Kora += [K]
    if(n == 0):
        KolKorabli2[b] -= 1
        KorabliKompa[b] += [Kora]
        KorabliKompa2[b] += [[ViborOs,Koor[0],Koor[1]]]
    else:
        KolKorabli[b] -= 1
        KorabliIgroka[b] += [Kora]
        KorabliIgroka2[b] += [[ViborOs,Koor[0],Koor[1]]]
i = 0
while((KolKorabli2[0]+KolKorabli2[1]+KolKorabli2[2]+KolKorabli2[3])>0):
    Postavit2(i,Pole2,0)
    if(KolKorabli2[i] <= 0):
        i += 1
        
def Splesh(Korabl,Osk,Pole2,KORKA):
    r = 1
    Koor = KORKA
    GU = 1
    F1 = 1
    F2 = 1
    F22 = 1
    B = Koor[1]+RazmerKorabl[Korabl]
    B2 = Koor[0]+RazmerKorabl[Korabl]
    if(Osk == 0 and B2<=9):
        if(Koor[1]-F1 < 0):
            F1=0
        else:
            F1=1
        if(Koor[1]+1 >= 10):
            F11=0
        else:
            F11=1
        if(Koor[0]-F2 < 0):
            F2=0
        else:
            F2=1
        if(Koor[0]+1 >= 10):
            F22=0
        else:
            F22=1
        for x in range(0,RazmerKorabl[Korabl]):
            for i in range(Koor[1]-F1,Koor[1]+F11+1):
                for j in range(Koor[0]-F2+x,(Koor[0]+F22)+x+1):
                    if(Pole2[i][j] != "▤"):
                        Pole2[i][j]="◈"
    if(Osk == 1 and B<=9):
        if(Koor[1]-F1 < 0):
            F1=0
        else:
            F1=1
        if(Koor[1]+1 >= 10):
            F11=0
        else:
            F11=1
        if(Koor[0]-F2 < 0):
            F2=0
        else:
            F2=1
        if(Koor[0]+1 >= 10):
            F22=0
        else:
            F22=1
        for x in range(0,RazmerKorabl[Korabl]):
            for i in range((Koor[1]-F1)+x,(Koor[1]+F11)+x+1):
                for j in range(Koor[0]-F2,Koor[0]+F22+1):
                    if(Pole2[i][j] != "▤"):
                        Pole2[i][j]="◈"

#Бой

print("Добро пожаловать в морской бой")
Avto = input("Вы желаете воспользоваться авто расстановкой?(Да, Нет) ")
if(Avto == "Нет"):
    Postavit()
else:
    too = 0
    while((KolKorabli[0]+KolKorabli[1]+KolKorabli[2]+KolKorabli[3])>0):
        Postavit2(too,Pole,1)
        if(KolKorabli[too] <= 0):
            too += 1

print("\nИГРА НАЧАЛАСЬ\n")
PoleBoy = [["▢"]*10 for i in range(10)]
Igrok = 20
Komp = 20
Hod = 0
def ViborMesto2(Pole):
    ViborKoordinti = input("Выберите место удара(Пример:А1) ")
    if(ViborKoordinti[1:] == "10"):
        Koor = [ViborKoordinti[:-2],ViborKoordinti[1:]]
    else:
        Koor = list(ViborKoordinti)
    if(Koor[0] not in Bykvi or int(Koor[1])>10):
        print("Неправильно введены координаты")
        return(ViborMesto2(Pole))
    else:
        Koor[0]=Koordinati[Bykvi.index(Koor[0])][0]
        if(Pole[int(Koor[1])-1][int(Koor[0])-1]=="▢"):
            return(Koor)
        else:
            print("Неправильно введены координаты")
            return(ViborMesto2(Pole))
Seria = 0
MaxSeria = 4
ch = 0
Ko = []
KoPer = []
Storon = 0
def LogikaKompa(Koor):
    global Hod
    global Igrok
    global Seria
    global MaxSeria
    global ch
    global Ko
    global KoPer
    global Storon
    c = 0
    K = [Koor[0],Koor[1]]
    Napr = [1,-1,1,-1]
    if(Seria < 2):
        Storona = randint(0,3)
    else:
        Storona = Storon
    r = 1
    f = 0
    for i in range(4):
        if(i < 2):
            if(K[0]+Napr[i]>9 or K[0]+Napr[i]<0):
                Napr[i]*=-1
        else:
            if(K[1]+Napr[i]>9 or K[1]+Napr[i]<0):
                Napr[i]*=-1
    for i in range(4):
        if(i < 2):
            if(Pole[K[1]][K[0]+Napr[i]]=="◈" or Pole[K[1]][K[0]+Napr[i]]=="▤"):
                f += 1
        else:
            if(Pole[int(K[1])+Napr[i]][K[0]]=="◈" or Pole[int(K[1])+Napr[i]][K[0]]=="▤"):
                f += 1
    if(f<4):
        f = 0
        while (r > 0):
            if(Storona < 2):
                K[0] += Napr[Storona]
            else:
                K[1] += Napr[Storona]
            if(Pole[K[1]][K[0]]!="◈" and Pole[K[1]][K[0]]!="▤"):
                r = 0
            else:
                K = [Koor[0],Koor[1]]
                Storona = randint(0,3)
        if(Pole[K[1]][K[0]] == "▢"):
            Pole[K[1]][K[0]]="◈"
            print(f"\nПротивник промахнулся [{Bykvi[K[0]+1]}{K[1]+1}]\n")
            if(c > 0):
                print("Выполнен СБРОС СЕРИИ")
                Seria = 0
                c = 0
            if(Seria > 1):
                Ko = KoPer
                c = 1
            Hod = 0
            ch = 1
        else:
            Pole[K[1]][K[0]]="▤"
            Igrok-=1
            Seria+=1
            os_new = 0
            koor_new = []
            for i in range(4):
                for j in range(len(KorabliIgroka[i])):
                    if([int(K[1]),int(K[0])] in KorabliIgroka[i][j]):
                        os_new = KorabliIgroka2[i][j][0]
                        koor_new = [KorabliIgroka2[i][j][1],KorabliIgroka2[i][j][2]]
                        KorabliIgroka[i][j].remove([int(K[1]),int(K[0])])
                        if(len(KorabliIgroka[i][j])>0):
                            print(f"\nПРОТИВНИК ПОПАЛ ПО ВАМ! [{Bykvi[K[0]+1]}{K[1]+1}]\n")
                            VivodPolaBoy(Pole,PoleBoy)
                            LogikaKompa(K)
                        else:
                            print(f"\nПРОТИВНИК УНИЧТОЖИЛ ВАШ КОРАБЛЬ! [{Bykvi[K[0]+1]}{K[1]+1}]\n")
                            ch = 0
                            Seria = 0
                            Splesh(i,os_new,Pole,koor_new)
                            VivodPolaBoy(Pole,PoleBoy)
            Ko = K
            Storon = Storona
            sleep(2.0)
            if(Seria < MaxSeria):
                LogikaKompa(K)
            else:
                MaxSeria-=1
                ch = 0
                Seria = 0
    else:
        HodKompa()
        Seria = 0
        ch = 0
def HodIgroka():
    global Hod
    global Komp
    VivodPolaBoy(Pole,PoleBoy)
    print("\nВаш ход\n")
    Koor = ViborMesto2(PoleBoy)
    if(Pole2[int(Koor[1])-1][int(Koor[0])-1] == "▢"):
        PoleBoy[int(Koor[1])-1][int(Koor[0])-1]="◈"
        Hod = 1
        print("\nМимо...\n")
        sleep(1.5)
    else:
        PoleBoy[int(Koor[1])-1][int(Koor[0])-1]="▤"
        os_new = 0
        koor_new = []
        for i in range(4):
            for j in range(len(KorabliKompa[i])):
                if([int(Koor[1])-1,int(Koor[0])-1] in KorabliKompa[i][j]):
                    os_new = KorabliKompa2[i][j][0]
                    koor_new = [KorabliKompa2[i][j][1],KorabliKompa2[i][j][2]]
                    KorabliKompa[i][j].remove([int(Koor[1])-1,int(Koor[0])-1])
                    if(len(KorabliKompa[i][j])>0):
                        print("\nПопадание!\n")
                    else:
                        print("\nУНИЧТОЖЕН!\n")
                        Splesh(i,os_new,PoleBoy,koor_new)
        Komp-=1
def HodKompa():
    global Hod
    global Igrok
    global Ko
    global KoPer
    global Seria
    Koor = [randint(0,9), randint(0,9)]
    r=1
    while(r >= 1):
        if(Pole[int(Koor[1])][int(Koor[0])]!="◈" and Pole[int(Koor[1])][int(Koor[0])]!="▤"):
            r=0
        else:
            Koor = [randint(0,9), randint(0,9)]
    if(Pole[int(Koor[1])][int(Koor[0])] == "▢"):
        Pole[int(Koor[1])][int(Koor[0])]="◈"
        print(f"\nПротивник промахнулся [{Bykvi[Koor[0]+1]}{Koor[1]+1}]\n")
        Hod = 0
    else:
        Pole[int(Koor[1])][int(Koor[0])]="▤"
        os_new = 0
        koor_new = []
        for i in range(4):
            for j in range(len(KorabliIgroka[i])):
                if([int(Koor[1]),int(Koor[0])] in KorabliIgroka[i][j]):
                    os_new = KorabliIgroka2[i][j][0]
                    koor_new = [KorabliIgroka2[i][j][1],KorabliIgroka2[i][j][2]]
                    KorabliIgroka[i][j].remove([int(Koor[1]),int(Koor[0])])
                    if(len(KorabliIgroka[i][j])>0):
                        print(f"\nПРОТИВНИК ПОПАЛ ПО ВАМ! [{Bykvi[Koor[0]+1]}{Koor[1]+1}]\n")
                        VivodPolaBoy(Pole,PoleBoy)
                        LogikaKompa(Koor)
                    else:
                        print(f"\nПРОТИВНИК УНИЧТОЖИЛ ВАШ КОРАБЛЬ! [{Bykvi[Koor[0]+1]}{Koor[1]+1}]\n")
                        Splesh(i,os_new,Pole,koor_new)
                        VivodPolaBoy(Pole,PoleBoy)
        Igrok-=1
        Seria+=1
        sleep(2.0)
        Ko = Koor
        KoPer = Koor
while (Igrok>0 and Komp>0):
    if(Hod == 0):
        HodIgroka()
    else:
        if(ch<1):
            HodKompa()
        else:
            LogikaKompa(Ko)
if(Igrok < 0):
    print("Вы проиграли... Серьёзно?")
else:
    print("Вы победили")