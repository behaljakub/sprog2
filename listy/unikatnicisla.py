import random

delka = int(input("Zadej délku seznamu: "))

cisla = []

for i in range(delka):
    cislo = random.randint(1, 100)
    cisla.append(cislo)

print(cisla)