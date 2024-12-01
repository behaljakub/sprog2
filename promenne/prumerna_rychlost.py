import math 

vzdalenost_km = float(input("Zadejte ujetou vzdálenost (km): "))
hodiny = int(input("Zadejte počet hodin: "))
minuty = int(input("Zadejte počet minut: "))
celkovy_cas = hodiny + minuty/60

prumer_rych = vzdalenost_km/celkovy_cas

print(f"Průměrná rychlost je: {prumer_rych} km/h")