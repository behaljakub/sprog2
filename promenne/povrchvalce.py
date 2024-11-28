import math
vyska = int(input("Výška Válce: "))
polomer = int(input("Polomer Válce: "))
vysledek = 2*math.pi*vyska*(polomer + vyska)
zaokrouhleno = round(vysledek,2)
print(f"Povrch Válce:", zaokrouhleno)