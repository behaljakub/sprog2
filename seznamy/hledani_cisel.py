import random

delka = int(input("Zadej délku seznamu: "))

cisla = []

for i in range(delka):
    cislo = random.randint(1, 10)
    cisla.append(cislo)

print(cisla)

target = int(input("Zadej číslo, které chceš najít: "))
misto = []

for x in range(len(cisla)):
    if cisla[x] == target:
        misto.append(x)
        
if misto:
    print(f"Číslo {target} se nachází na indexech: {misto}")
else:
    print(f"Číslo {target} v seznamu není.")