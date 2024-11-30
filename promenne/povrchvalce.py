import math
height = float(input("Výška Válce: "))
radius = float(input("Polomer Válce: "))
result = 2*math.pi*height*(radius + height)
print(f"Povrch Válce:, {result} cm²")