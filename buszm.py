
jegy=[]
def F1():
    
    fbe=open('eladott.txt', 'r')
    elsosor=fbe.readline()
    elsosor=elsosor.strip().split()
    global ej, tav, ar
    ej=int(elsosor[0])
    tav=int(elsosor[1])
    ar=int(elsosor[2])

    for sor in fbe:
        sor=sor.strip().split()
        for i in range (3):
            sor[i]=int(sor[i])
        jegy.append(sor)
        
        fbe.close




def F2():
    print('2.Feladat')
    print('Az utolsó jegyvásárló ülése:%d, megtett távolság:%d' %(jegy[-1][0],jegy[-1][2]-jegy[-1][-1]))

def F3():
    print('3.feladat')
    print('Akik végig utaztak:',end='')

    for i in range(ej):
        if jegy[i][1]==0 and jegy [i][2]==tav:
            print(i+1,end=' ')

def F4_1():
    bevetel=0   
    for utas in jegy:
        km=utas[2]-utas[1]
        tiz=int(km/10)
        if km%10>0:
            tiz+=1
        fizet=tiz*ar
        maradek=fizet%5
        if maradek<3:
            fizet=fizet-maradek
        else:
            fizet=fizet-maradek+5
        bevetel+=fizet
    print("nyereség:",bevetel)

def F5():
    h= set()
    for i in range(len(jegy)-1):
        h.add(jegy[i][1])
        h.add(jegy[i][2])
    l=list(h)
    l=sorted(l)
    print("6. feladat:",(len(l)-2),("megálló volt a végek között"))
    kérdés=l[-2]
    k=0
    for i in range (len(jegy)):
        if jegy[i][2] == kérdés:
            k+=1
        if jegy[i][1] == kérdés:
            k+=1
    print("5. feladat",k)
        
        
def F7():
    ulesek=[0]*48
    hely=int(input("7. Feladat\n Ird be a kilómétert:"))
    for i in range(len(jegy)):
        if jegy[i][1]<=hely and jegy[i][2]>hely:
            ulesek[jegy[i][0]-1]=i+1
    print(ulesek)


    for i in range( len(ulesek)):
        if ulesek[i]==0:
            print(i+1,'ülés: üres')
        else:
            print(i+1,'ülés:',ulesek[i],'.utas')


F1()
F2()
F3()
F4_1()
F5()

F7()
