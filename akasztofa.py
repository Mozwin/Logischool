kepek = ['''

=========''','''
      |
      |
      |
      |
      |
      |
=========''','''
  ----+
      |
      |
      |
      |
      |
========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

feladvany = "az almafa egy cipo"
megoldas = ""
helyes_karakterek = []
helytelen_karakterek = []
elet = 10
for i in feladvany:
    if i == " ":
        megoldas += " "
    else:
        megoldas += "*"
#maga a jatek
while elet > 0 and megoldas != feladvany:
    print(megoldas)
    tipp = input("\nTippelj:")
    if len(tipp) == len(feladvany):
        if tipp == feladvany:
            megoldas = tipp
        else:
            elet -=1
            print(kepek[9-elet])
            print(f"\nNem találtad el, már csak {elet} lehetőséged")
    elif len(tipp) == 1:
        if tipp in feladvany:
            for i in range (len(feladvany)):
                if feladvany[i] == tipp:   #bepakolas, ha eltalaltam
                    temp = list(megoldas)
                    temp[i] = tipp
                    megoldas = "".join(temp)
            helyes_karakterek.append(tipp)
        else:
            helytelen_karakterek.append(tipp)
            elet-= 1
            print(kepek[9-elet])
            print(f"Nincs ilyen betű a megfejtésben, marad még {elet} lehetőséged")
        print(f"Helytelen karakter(ek): {','.join(helytelen_karakterek)} ")
if elet > 0:
    print("Ön nyert")
else:
    print("Majd legközelebb")
input()

