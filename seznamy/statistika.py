import random

delka = int(input("Zadej délku seznamu: "))

cisla = []

for i in range(delka):
    cislo = random.randint(1, 100)
    cisla.append(cislo)

print("Vygenerovaný seznam:", cisla)

maxn = cisla[0]
minn = cisla[0]

for i in cisla:
    if i > maxn:
        maxn = i

print(maxn)

for n in cisla:
    if n < minn:
        minn = n 

print(minn)

soucet = 0

for k in cisla:
    soucet += k

print(soucet/len(cisla))


    



