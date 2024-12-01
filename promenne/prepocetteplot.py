import math

c = float(input("Hodntoa teploty (C): "))
prevodF = c*9/5 + 32
prevodK = c + 273.15
roundoffF = round(prevodF, 2)
roundoffK = round(prevodK, 2)

print(f"Hodnota ve Fahrenheitech: ",roundoffF)
print(f"Hodnota v Kelvinech ", roundoffK)
