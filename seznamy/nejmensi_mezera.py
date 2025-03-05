import random

delka = int(input("Zadej délku seznamu: "))

cisla = []

for i in range(delka):
    cislo = random.randint(1, 10)
    cisla.append(cislo)

print(cisla)

nejmensi_rozdil = float('inf')

for i in range(1, len(cisla)):
    rozdil = cisla[i] - cisla[i - 1]
    if rozdil < nejmensi_rozdil:
        nejmensi_rozdil = rozdil

print("Nejmenší rozdíl mezi dvěma sousedními čísly v seřazeném seznamu je:", nejmensi_rozdil)