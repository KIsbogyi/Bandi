cég = []
fbe = open('autok.txt' , 'r')
for sor in fbe:
    sor = sor.strip().split()
    cég.append(sor)
print(cég)


def F2():
    i=len(cég)-1
    while cég[i][5]!='0':
        i-=1
    print(cég[i][0]+'.nap rendszám:'+cég[i][2])


def F3():
    x=input('Hányadik napot kéred?')
    for kislista in cég:
        if kislista[0] == x:  
            print(kislista[1]+' '+kislista[2]+' '+kislista[3],end=' ')
            if kislista[5] == '0':
                print('ki')
            else:
                print('be')
def F4():
    autó = ['0']*10
    for i in cég:
        index=int(i[2][5])
        autó[index] = i[5]
    print('A hónap végén %d autót nem hoztak vissza' %autó.count('0'))   #%jel azt mondja hogy változót írunk ki második pedíg a váltózót jelöli


def F5():
    autokm=[0]*10
    for i in range(10):
        rsz='CEG30'+str(i)
        j=0
        while rsz != cég[j][2]:     #elösször hol van az auto
            j+=1
            
        k=len(cég)-1
        while rsz != cég[k][2]:     #utoljára hol van az autó
            k-=1

        autokm[i]=int(cég[k][4])-int(cég[j][4])
    print(autokm)
        




 #heineken#heineken#heineken#heineken#heineken#heineken#heineken#heineken
F2()
F3()
F4()
F5()
