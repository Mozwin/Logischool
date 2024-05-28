import random
for i in range (10):
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    eredmeny = x * y
    bekertszam = int(input(f"{x} * {y} = "))
    if bekertszam == eredmeny:
        print("Helyes!")
    else:
        print("Rossz!")
