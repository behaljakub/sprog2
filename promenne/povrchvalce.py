import math
height = float(input("Výška Válce: "))
radius = float(input("Polomer Válce: "))
vysledek = 2*math.pi*height*(radius + height)
roundedoff = round(vysledek,2)
print(f"Povrch Válce:, {roundedoff} cm²")