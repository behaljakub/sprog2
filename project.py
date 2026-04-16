import random

delka = int(input("Zadej délku seznamu: "))

cisla = []
for i in range(delka):
    cislo = random.randint(1, 20)
    cisla.append(cislo)

print(cisla)

novy_seznam = []

for x in cisla:
    if cisla.count(x) == 1:
        novy_seznam.append(x)
  
print(novy_seznam)