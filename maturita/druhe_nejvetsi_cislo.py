import random

delka = int(input("Zadej délku seznamu: "))

cisla = []

for i in range(delka):
    cislo = random.randint(1, 10)
    cisla.append(cislo)

print(cisla)

max = cisla[0]
min = cisla[0]

for x in cisla:
    if x > max:
        max = x
    
    if x < min:
        min = x

druhy_nejvetsi = min

if max == min:
    print("nelze")

for i in range(len(cisla)):
    if cisla[i] > druhy_nejvetsi and cisla[i] < max:
        druhy_nejvetsi = cisla[i]


print(druhy_nejvetsi)


#dodelat doma metodou seznam bez nejvetsiho



