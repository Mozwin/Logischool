# bekér 3 számot a felhaszn-tól melyik legnagyobb? kiiratja a választ: hogy meylik a legnagyobb

a = float(input("add meg az elso szamot:"))
b = float(input("add meg a masodik szamot:"))
c = float(input("add meg a harmadik szamot:"))

if a > b:  #itt az a legnagyobb
    if a > c:
      # print(f" {a} a legnagyobb szam ")
        print(str(a) + " a legnagyobb szam ")
    elif a < c:  # c>a:
        print(str(c) + " a legnagyobb szam ")
    else:
        print("több lehetőség van")
elif b > a:      #itt a b legnagyobb
    if b > c:
        print(str(b) + " a legnagyobb szam ")
    elif c > b:
        print(str(c) + " a legnagyobb szam ")
    else:
        print("több lehetőség van")
else: #itt az c legnagyobb
    if c > b:
        print(str(c) + " a legnagyobb szam ")
    else:
        print(" nincs eleg info")
