shopping_list = ["alma", "tej", "kenyér"]
my_friends = ["Anna", "Peti", "Gergő", "Béla", "Sanyi"]
print(shopping_list)
print(my_friends + shopping_list)

i = 0
while i < len(my_friends):
    print(my_friends[i])
    i +=1

print("\n".join(my_friends))
print("")

#muveletek
shopping_list.append("kóla")
print(shopping_list)

shopping_list.insert(0,"retek")
print(shopping_list)

print(shopping_list[2])
print(shopping_list[-2])

print(len(shopping_list))

shopping_list.remove("tej")
#del shopping_list[shopping_list.index("alma")]
print(shopping_list)

shopping_list[shopping_list.index("kóla")] = "banán"
print(shopping_list)

shopping_list.pop(2)
print(shopping_list)

print(shopping_list[len(shopping_list) // 2 ])

#lista feltotése ciklussal
szamok = []
i=0
while i<7:
    szamok.append(i)
    i +=2
print(szamok)

szamok.insert(1, -1)
szamok.insert(20, 8)
szamok.insert(15, 7)
print(szamok)

numbers = [1,2,0,0,1,0,2,0,0,1,0,2,1,1,0,2]  # 0. - numbers[0]

print(numbers)
value = int(input("Melyik erteket szamoljam meg?"))
i = 0
elofordulasok = 0
print(value)
while i<len(numbers):
    if numbers[i] == value:
        elofordulasok +=1
    i+=1
print(f"elofordulasok szama hosszan: {elofordulasok}")

print(f"elofordulasok szama röviden: {numbers.count(value)}")

numbers = [1,2,0,0,1,0,2,0,0,1,0,2,1,1,0,2]  # 0. - numbers[0]
osszeg = 0
j = 0
while j<len(numbers):
    osszeg += numbers[j]
    j+=1

print(f"osszeg hosszan: {osszeg}")

print(f"osszeg röviden: {sum(numbers)}")