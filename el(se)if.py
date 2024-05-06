number=2
if number == 10:
    print("egyenlo")
else:
    print("nem egyenlo")

status = 100   # ő a kevésbé optimális megoldás
if status == 100:
    print("continue")
if status == 200:
    print("ok")
if status == 300:
    print("multiple choises")

status2 = 200   # ő az optimális megoldás
if status2 == 100:
    print("continue")
elif status2 == 200:
    print("ok")
elif status2 == 300:
    print("multiple choises")

status3 = 200   # ő meg egy másik
match status3:
    case 100:
        print("continue")
    case 200:
        print("ok")
    case 300:
        print("multiple choises")
    case _:
        print("valami")