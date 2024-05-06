email = input("Add meg az emailed: ")
if '@' in email and (email.endswith(".com") email.endswith(".hu")):
    print("ervenyes")
else:
    print("nem ervenyes")