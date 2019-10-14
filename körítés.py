adat=[]
def F1():
    hsz_ps=2
    hsz_pt=1
    fbe=open('kerites.txt','r')
    for sor in fbe:
        sor=sor.strip().split()
        if sor[0]=='0':
            sor.append(hsz_ps)       
            hsz_ps+=2
        else:
            sor.append(hsz_pt)
            hsz_pt+=2
        adat.append(sor)
    fbe.close
def F2():
##    for i in range(len(adat)):
##        if adat[i][0]=='0':
##            print(adat[i])
##    for elem in  adat:
##        if elem[0]=='0':
##            print(elem[2])
    print('eladtott telkek száma:', len(adat))
def F3():
    print('A harmadik feadat:')
    if adat[-1][0]=='0':
        print('apáros oldalon adták el az utolsó telket')
    else:
       print('apáratlan oldalon adták el az utolsó telket')
    print('az utolsó telek házszáma:', adat[-1][3])
def F4():
    oldal=[]
    for i in range(len(adat)-1):
        if adat[i][0]=='1':
            
            print('egyezik:', oldal[i][3])
            break
        
        
    #2018okt emelt
    
    
#-*--*-**--*-*-*--**-*-*-*-*-**-*-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-*-*
F1()
F2()
F3()
F4()
F5()
F6()
F7()

