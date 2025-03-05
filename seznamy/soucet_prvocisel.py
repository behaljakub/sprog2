import random

delka = int(input("Zadej délku seznamu: "))

cisla = []

for i in range(2, delka):
    cisla.append(i)

for i in cisla:
        for j in range(i*2, delka + 1, i):
            if j in cisla:
                cisla.remove(j)

print(cisla)

cislo = 0

for x in cisla:
     cislo += x

print(cislo)