import random

delka = int(input("Zadej délku seznamu: "))

cisla = []

for i in range(delka):
    x = random.randint(1, 100)
    cisla.append(x)

print(f"První (náhodný) seznam: {cisla}")

c1 = int(input("Zadejte 1. číslo: "))
c2 = int(input("Zadejte 2. číslo: "))
#c3 = int(input("Zadejte 3. číslo: "))
#c4 = int(input("Zadejte 4. číslo: "))
#c5 = int(input("Zadejte 5. číslo: "))
a = [c1, c2,]

print(f"Druhý (uživatelský) seznam: {a}")

spolc = []
index = 0

for x in cisla:
    if x in a:
        spolc.append(x)
        index += 1

if index == 0:
    print("Není")
else:
    print(spolc)
    print(index)

    maxn = spolc[0]
    minn = spolc[0]

    for z in spolc:
        if z > maxn:
            maxn = z
    print(maxn)




