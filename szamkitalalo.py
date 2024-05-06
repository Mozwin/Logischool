import random
szam = random.randint(1, 100)
probalkozasok = 5
tipp = int(input("Adj meg egy számot 1 - 100 között: "))

while probalkozasok > 0 :
    probalkozasok-=1
    if tipp < szam :
        print("nagyobbat")
    elif tipp > szam :
        print("kisebbet")
    else:
        print("kitalaltad")
        break
    if szam != tipp:
        tipp = int(input("Adj meg egy számot 1 - 100 között: "))
