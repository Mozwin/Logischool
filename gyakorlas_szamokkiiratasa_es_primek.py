# számok kiiratasa 1-100ig
szam = 1
while szam<=100: #<101
    print(szam)
    szam+=1

#prímszámok 1-100ig
number=2
while number < 100:
    oszto = 2
    prim_e = True
    while oszto < number and prim_e:
        if number % oszto == 0:
            prim_e = False
        oszto+=1
    if prim_e:
        print(number)
    number+=1

#számolja össze a számjegyeket
szam = int(input("Adj meg egy nagy számot: "))
db = 0
while szam != 0:
    szam//=10
    db+=1
print(f"{db} számjegyet adtál meg")