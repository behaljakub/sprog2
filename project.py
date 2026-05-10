import random

delka = int(input("zadejte delku seznamu: "))
cisla = []

for i in range(delka):
    cislo = random.randint(1, 100)
    cisla.append(cislo)

print(cisla)

max = cisla[0]
misto = []
for x in cisla:
    if x > max:
        max = x

print(max)

target = max
misto = 0
for x in range(len(cisla)):
    if cisla[x] == target:
        misto = x

print(misto)

seznam_bez_indexu = cisla.pop(misto)

print(cisla)

druhy_nejvetsi = cisla[0]
for x in cisla:
    if x > druhy_nejvetsi:
        druhy_nejvetsi = x

print(druhy_nejvetsi)






