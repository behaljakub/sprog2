zaklad = int(input("Zadejte základ:"))
exponent = int(input("Zadejte exponent: "))

cislo = zaklad

for x in range(exponent - 1):
    cislo*= zaklad

print(cislo)