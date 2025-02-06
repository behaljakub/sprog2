import math

height = float(input("Výška Válce(cm): "))
radius = float(input("Polomer Válce(cm): "))
result = 2*math.pi*height*(radius + height)

print(f"Povrch Válce:, {result} cm²")