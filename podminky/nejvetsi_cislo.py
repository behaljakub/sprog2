import math

cislo1 = float(input("Zadejte první číslo: "))
cislo2 = float(input("Zadejte druhé číslo: "))
cislo3 = float(input("Zadejte třetí číslo: "))

if cislo1 > (cislo2 and cislo3):
    print(f"Číslo {cislo1} je největší")
elif cislo2 > (cislo1 and cislo3):
    print(f"Číslo {cislo2} je nejvetší")
elif cislo3 > (cislo1 and cislo2):
    print(f"Číslo {cislo3} je největší")