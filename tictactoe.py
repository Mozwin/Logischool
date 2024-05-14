tabla = []
for i in range (3):
    sor = []
    for j in range (3):
        sor.append(" ")
    tabla.append(sor)   #tablaba sort töltöttünk, sorba szóközöket
player1 = True
game = True
while game:
    print("\n  1 2 3")
    for i in range (len(tabla)):
        print(f"{i+1}|", end="")
        for j in range (len(tabla[i])):  # i. elem igazabol sor
            print(tabla[i][j], end="|")  #mtxosan kiirattuk a listaban a listat
        print()
    print(f"{'1.' if player1 else '2.'} jatekos jön") #vicces elágazás (mag csak 1 sor, mehet egybe minden)
    jo_lepes = False
    while not jo_lepes:
        sor = int(input("Melyik sorba rakjam?"))
        while sor < 1 and sor > 3:
            sor = int(input("Melyik sorba rakjam?"))
        oszlop = int(input("Melyik oszlopba rakjam?"))
        while oszlop < 1 and oszlop > 3:
            oszlop = int(input("Melyik oszlopba rakjam?"))
        if tabla[sor - 1][oszlop -1] == " ":
            jo_lepes = True
        else:
            print("Nem érvényes mezőt választottál")
    tabla[sor - 1][oszlop -1] = "x" if player1 else "o"
    # nyertem, vesztettem, döntetlen
    for i in range(3):
        if game and (tabla[i][0] != " " and tabla[i][0] == tabla[i][1] and tabla[i][1] == tabla[i][2] or tabla[0][i] != " " and tabla[i][0] == tabla[1][i] and tabla[1][i] == tabla[2][i]):
            game = False
            print(f"{'1.' if player1 else '2.'} jatekos nyert")
        # keresztbe nyeres
    if game and (tabla[0][0] != " " and tabla[0][0] == tabla[1][1] and tabla[1][1] == tabla[2][2] or tabla[0][2] != " " and tabla[0][2] == tabla[1][1] and tabla[1][1] == tabla[2][0]):
        game = False
        print(f"{'1.' if player1 else '2.'} jatekos nyert")
        # döntetlen
    if " " not in tabla[1] and " " not in tabla[1] and " " not in tabla[2]:
        game = False
        print("Döntetlen")
    # 2. jöjjön az elso utan
    if game:
        player1 = not player1
print()
# tablatörlés plusz feladat
