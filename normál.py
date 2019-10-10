tarsalgo=[]
emberek=[0]*100
def F1():
    fbe=open("ajto.txt", 'r')
    for sor in fbe:
        sor=sor.strip().split()
        tarsalgo.append(sor)
    fbe.close

def F2():
    for kislista in tarsalgo:
        if kislista [3]=="be":
            print("első belépő", kislista[2])
            break
    index=0
    while tarsalgo[index][3]!="be":
        index+=1
    print("első belépő", tarsalgo[index][2])


    for index in range(len(tarsalgo)-1,-1,-1):
        if tarsalgo[index][3]=="ki":
            print('utcsó:', tarsalgo[index][2])
            break


def F3():
    
    for kislista in tarsalgo:
        index=int(kislista[2])-1
        emberek[index]+=1
        fki=open("áthaladás.txt", 'w+')
        for i in range (len(emberek)):
            if emberek[i]!=0:
                fki.write(str(i+1)+' '+str(emberek[i])+"\n")
        fki.close            

    print(emberek)


def F4():
    print('bentmaradtak:')
    for i in range(100):
        if emberek[i]!=0 and emberek[i]%2==1:
            print(i+1, end=' ')
    
        
        
    
F1()
F2()
F3()
F4()
