
a = int(input("Zadejte první cislo: "))
b = int(input("Zadejte druhe cislo: "))
operation = input("+, -, *, /: ")
if operation == "+":
    print(a + b)

elif operation == "-":
    print(a - b)

elif operation == "*":
    print(a * b)

elif operation == "/":
    if b == 0:
        print("Error, nelze delit nulou")
    else:
        print(a / b)