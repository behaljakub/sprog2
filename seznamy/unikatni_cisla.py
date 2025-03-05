import random

delka = int(input("Zadej délku seznamu: "))

cisla = []
for i in range(delka):
    cislo = random.randint(1, 10)
    cisla.append(cislo)

print("Vygenerovaný seznam:", cisla)


unikatni_hodnoty = [x for x in cisla if cisla.count(x) == 1]

print(unikatni_hodnoty)