import math

volume = float(input("Objem dat v MB: "))
speed = float(input("Rychlost stahovaní v Mbit/s: "))
time = (volume*8)/(speed)
roundoff = round(time, 2)

print(f"Doba stáhování je: {roundoff}s")

