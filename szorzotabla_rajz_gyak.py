#szorzótábla vicces módon, lista osztása- lista a listaban

#lista számokkal 1-10ig, ciklusal feltöltve

numbers=[]
for i in range(1,11):
    for j in range (1,11):
        numbers.append(i*j)
#print(numbers)
j=0
for i in range (11): #szépen nyomtatni: i * j = eredmény = numbers[i']
    print(numbers[i*10 : (i*10) + 10]) # 10 elemenkent szeretnem felosztani a listat
    j+=1