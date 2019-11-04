#feladat: beolvasunk a,b,c egész számokat, lehet-e háromszög ezekből? Derékszögű-e?
lst=[]
for i in range(3):
    lst.append(int(input(str(i+1)+'oldal')))
    lst=sorted(lst)
    
if lst[0]+lst[1]>lst[2]:
    print('lehet ilyen háromszög')
    
    if lst[0]^2+lst[1]^2==lst[2]^2:
        print('derékszögű')

def hossz(data):
    return len(data)
    
fbe=open('szotar.txt','r')
lista=[]
for k in fbe:
    lista.append(k.strip())
    

fbe.close()
print(lista)

print('lista elemeinek száma:', len(lista))
rlista=sorted(lista,key=hossz,reverse=True)
print(rlista)
print('a leghosszabb szó:',rlista[0],end=' ')
while len(rlista[i])==len(rlista[0]):
    print(rlista[i], end=' ')
    i+=1
