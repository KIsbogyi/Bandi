import math
lst=[]
def F1():
    print('beolvasom a programot pls stand by')
    fbe=open('program.txt', 'r')
    global p
    p=int(fbe.readline())
    for k in fbe:
        lst.append(k.strip())
    print(lst)
    fbe.close()

def F2():
    usz=int(input('kérem egy utasítás sorszámát'))
    print('vizsgálat tárgya:',lst[usz-1])
    prg=lst[usz-1]
    van=False
    nincs=True
    i=0
    h=set()
    h={'ED', 'DE' ,'KN', 'NK'}
    while i<len(prg)-1 and nincs:
        s=prg[i]+prg[i+1]
        if s in h:
            nincs=False
            break
        i+=1
    if nincs:
        print('nem egyszerűsithető')
    else:
        print('egyszerűsithető')



    x=0
    y=0
    maxi_tav=0
    lepes=0
    for i in range(len(prg)):
        if prg[i]=='E':
            y+=1
        if prg[i]=='D':
            y-=1
        if prg[i]=='N':
            x+=1
        if prg[i]=='K':
            x-=1
        c=math.sqrt(x**2+y**2)
        if c>maxi_tav:
            maxi_tav=c
            lepes=i+1

    print(abs(y),'lépést kell tenni x-tengelyen')
    print(abs(x),'lépést kell tenni y-tengelyen')
    print('a legnagyobb táv a %d. lépésben: %.3f' %(lepes,maxi_tav))

def F3():
    h=set()
    h={'EN', 'EK', 'DN', 'DK', 'NE','KE', 'ND','KD'}
    ind=2
    for sorsz in range(len(lst)):
        e=0
        for i in range(len(lst[sorsz])-1):
            e+=1
            if lst[sorsz][i]+lst[sorsz][i+1] in h:
                e+=2
        e+=ind
        if e<=100:
            print(sorsz+1,' ',e)

def F4():
    fki=open('ujprog.txt', 'w+')
    sz=1
    ujsz=''
    for prg in lst:
        for i in range(len(prg)-1):
            if prg[i]==prg[i+1]:
                sz+=1
            else:
                if sz==1:
                    ujsz+=prg[i]
                else:
                    ujsz+=str(sz)+prg[i]
                sz=1
        if sz==1:
            ujsz+=prg[-1]
        else:
            ujsz+=str(sz)+prg[i]
        print(ujsz)
        fki.write(ujsz+'\n')
        ujsz=''
    fki.close
            
        
        
        

    
#g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2
F1()
F2()
F3()
F4()
