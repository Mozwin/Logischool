#maximum kereses tetele

kenyer = ["rozskenyer", "barnakenyer", "feherkenyer", "simakenyer", "kovaszoskenyer", "magvaskenyer", "kenyeraroma", "lilakenyer", "majomkenyer"]
arak = [600, 650, 720, 580, 610, 610, 705, 1000, 710]
#max = max(arak)
max = max(arak)
for i in range(len(arak)):
    if arak[i] == max:
        print(f"A legdragabb kenyer: {kenyer[i]}, {max} Ft/kg")

#összegzes tetele
n = int(input("hany számot összegezzek?"))
sum = 0
for i in range (n+1):
    sum += i # 0+1=1, 1+2 = 3, 3+3 = 6, 6+4 = 10...
print(f"Az összeg: {sum}")
