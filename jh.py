uzenetek=[]
def beolvas():
    fbe=open('sms.txt' ,'r')
    global usz
    usz=int(fbe.readline())
    x=1
    
    for sor in fbe:
        if x==1:
            uz1=sor.strip().split()
            x=2
        else:
            sor=sor.strip()
            uz2=[]
            uz2.append(sor)
            uzenetek.append(uz1+uz2)
            x=1
    fbe.close()
    print(uzenetek)
def friss():
    if usz>10:
        print(uzenetek[9][3])
    else:
        print(uzenetek[-1][3])
def legek():
    def uz_hossza(kislista):
        return len(kislista[3])
    rendezett=sorted(uzenetek, key=uz_hossza)
    print(rendezett)
    print('legrövediebb üzi',rendezett[0])
    print('leghosszabb üzi',rendezett[-1])

def hossz():
1.=[]
2.=[]
3.=[]
4.=[]
5.=[]
    for sor in uzenetek:
        if len(sor)<20 1.
        if len(sor)<40 and len(sor)>21 
        if len(sor)<60 and len(sor)<41
        if len(sor)<80 and len(sor)<61
        if len(sor)<100 and len(sor)<81
        
        





beolvas()
friss()
legek()
