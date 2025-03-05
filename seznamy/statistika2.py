import random

delka = int(input("Zadej délku seznamu: "))

cisla = []

for i in range(delka):
    cislo = random.randint(1, 10)
    cisla.append(cislo)

print(cisla)

for i in range(len(cisla)):
    for j in range(i + 1, len(cisla)):
        if cisla[i] == cisla[j]:
            print(f"Číslo {cisla[i]} se opakuje na indexech {i} a {j}")

