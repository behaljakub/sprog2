import random

delka = int(input("Zadej délku seznamu: "))

cisla = []

for i in range(delka):
    cislo = random.randint(1, 100)
    cisla.append(cislo)

print(f"První (náhodný) seznam: {cisla}")

c1 = int(input("Zadejte 1. číslo: "))
c2 = int(input("Zadejte 2. číslo: "))
c3 = int(input("Zadejte 3. číslo: "))
c4 = int(input("Zadejte 4. číslo: "))
c5 = int(input("Zadejte 5. číslo: "))
a = [c1, c2, c3, c4, c5]

print(f"Druhý (uživatelský) seznam: {a}")

#Zjištění spolčných čísel a počtu           
spolecna_cisla = []
count_spol = 0
for cislo in cisla:
    if cislo in a:
        spolecna_cisla.append(cislo)
        count_spol += 1

if count_spol == 0:
    print("Žádné společné číslo")
else:
    print(f"Společná čísla: {spolecna_cisla}")
    print(f"Počet společných čísel: {count_spol}")

    #největší a nejmenší spol. číslo
    maxn = spolecna_cisla[0]
    minn = spolecna_cisla[0]

    for k in spolecna_cisla:
        if k > maxn:
            maxn = k

    for l in spolecna_cisla:
        if l < minn:
            minn = l
    print(f"Největší společné číslo: {maxn}")
    print(f"Nejmenší společné číslo: {minn}")

    #Součet spol. čísel
    soucet_spol = 0
    for u in spolecna_cisla:
        soucet_spol += u
    print(f"Součet společných čísel: {soucet_spol}")

#Průměr hodnot
soucet = 0
for x in cisla:
    soucet += x
print(f"Průměr prvního seznamu: {soucet/len(cisla)}")

#Počet čísel větší než 50
count = 0
for y in a:
    if y > 50:
        count += 1
print(f"Počet čísel v druhém seznamu větších než 50: {count}")