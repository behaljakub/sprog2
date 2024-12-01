import math

height = float(input("Výška válce (cm): "))
radius = float(input("Poloměr válce (cm): "))
result = int(math.pi*radius**2*height)
roundedoff = round(result,2)

print(f"Výsledkem je: {roundedoff} cm³.")