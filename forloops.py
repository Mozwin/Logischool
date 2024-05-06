for i in range(10):
    print(i)
print("---")

#kezdeti értékkel for loop
for i in range(1,10):
    print(i)
print("---")

for i in range(2,50,2):
    print(i)
print("---")

for i in range(10,0,-1):
    print(i)
print("---")

for i in "Hello World":
    print(i)
print("---")

#lista bejarasa 2felekepp
szamok = [1, 8, 3, 87, 2, -10, 0, 1 , 2]

for i in range (0, len(szamok)):
    print(szamok[i])
print("---")

for i in szamok:
    print(i)

#szorzótábla
num = int(input("adj meg egy szamot es megadom a szorzatait 10-ig:"))
for i in range (1,11,1):
    print(str(i) + "*" + str(num) + "=" + str(i*num))