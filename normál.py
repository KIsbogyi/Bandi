tarsalgo = []
emberek = [0]*100
bent = []
def F1():
    fbe =  open("ajto.txt", 'r')
    for sor in fbe:
        sor=sor.strip().split()
        tarsalgo.append(sor)
    fbe.close


def F2():
    for kislista in tarsalgo:
        if kislista [3] == "be":
            #print("első belépő", kislista[2])
            break
    index = 0
    while tarsalgo[index][3] != "be":
        index += 1
    print("1. feladat: első belépő", tarsalgo[index][2])


    for index in range(len(tarsalgo)-1,-1,-1):
        if tarsalgo[index][3] == "ki":
            print('2. feladat: utcsó:', tarsalgo[index][2])
            break


def F3():
    
    for kislista in tarsalgo:
        index = int(kislista[2])-1
        emberek[index] += 1
        fki = open("áthaladás.txt", 'w+')
        for i in range (len(emberek)):
            if emberek[i] !=0:
                fki.write(str(i+1)+' '+str(emberek[i])+"\n")
        fki.close()            

    print('3. feladat kész csak nem látod')


def F4():
    print('4. feladat és bentmaradtak:')
    for i in range(100):
        if emberek[i] != 0 and emberek[i]%2 == 1:
            print(i+1 , end = ' ')
    print('')


def F5():
    sz = 0
    b = 0
    for sor in tarsalgo:
        if sor[3] == 'be':
            sz += 1
        else:
            sz -= 1
        egylista = []
        egylista.append(int(sor[0]))
        egylista.append(int(sor[1]))
        egylista.append(int(sz))
        bent.append(egylista)

    
    for k in bent:
        if k[2] > b:
            b = k[2]
            ora = k[0]
            perc = k[1]
    
    print(ora,':',perc,'. kor voltak a legtöbben')


def F6():
    global x
    x = int(input('Azonosítót kérek: '))


def F7():
    cs = 0
    for sor in tarsalgo:
        
        if int(sor[2]) == x and sor[3] == 'be':
            print("{}:{}-".format(sor[0], sor[1]) , end = '')
            óra = int(sor[0])
            perc = int(sor[1])
            l = 0
        if int(sor[2]) == x and sor[3] == 'ki':
            print("{}:{}".format(sor[0], sor[1]))
            z = int(sor[0])-óra
            k = int(sor[1])-perc
            cs += z*60+k
            l = 1
    print('')
    
    if l == 0:
        cs += (15-óra)*60
        cs += (0-perc)
        print(cs)
        
    
            

        
        
            
        


    
        
        
        
    
        
        
    
F1()
F2()
F3()
F4()
F5()
F6()
F7()
