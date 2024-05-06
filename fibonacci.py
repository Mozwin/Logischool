fib =int(input("Hány Fibonacci számra vagy kíváncsi?"))
szam1=0
szam2=1
while fib>0:
    print(szam1)
    temp=szam1 + szam2
    szam1=szam2
    szam2=temp
    fib-=1
print()