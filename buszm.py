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
        
    










F1()
F2()
F3()
