#collatz sejtés: minden pozitiv egesz szam 1-é redukalhato két művelet ismétlése segítségével

szam = int(input()) #maga a szam amit eggyé szeretnenk alakitani
collatz = []  #folyamat szamai egy listaban
#maga a művelet
while szam!=1:
    if szam % 2 ==0: #paros a szam -> /2
        szam/=2
        collatz.append(int(szam)) #listaba tesszuk, hogy lássuk a köztes állapotokat
    else:
        szam = 3*szam+1 #paratlan eset szabalya : (szam*3)+1
        collatz.append(int(szam))
print(collatz)
