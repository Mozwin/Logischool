#pozitiv - e
szam = float(input("adj meg egy szamot: "))
if szam >= 0:
    print("pozitiv")
else:
    print("negativ")

# listában szerepel-e egy nev
# hint: string.lower(), .upper() fv-ek
#for item in list/names:

names = ["Gyula", "Béla", "Lajos", "János", "Pista", "Péter", "Brendon", "Marika"]
benne_van = False  #kérésre random jelentés nélküli komment: Fólx
valaki = input("adj meg egy nevet: ")

for item in names:
    if valaki.lower() == item.lower():
        benne_van = True
#kiiratás - plusz feladat

#csere index alapján egy listában, indexeket bekérve és az alapján - még plusszabb feladat
