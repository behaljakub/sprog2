import math

def kvadraticka_rovnice(a, b, c):
    # Zde napiš svůj kód
    # 1. Vypočítej diskriminant D = b² - 4ac
    D = b**2 - 4*a*c
    # 2. Pokud D < 0, vrať None
    if D < 0:
        return None
    # 3. Pokud D >= 0, vypočítej oba kořeny
    elif D >= 0:
        koren1 = (-b + math.sqrt(D))/2*a
        koren2 = (-b - math.sqrt(D))/2*a
    # 4. Vrať x1, x2
        return koren1, koren2
    pass

# Příklad použití
print(kvadraticka_rovnice(1, -5, 6))  # Očekávaný výstup: (3.0, 2.0)
print(kvadraticka_rovnice(1, -4, 4))  # Očekávaný výstup: (2.0, 2.0)
print(kvadraticka_rovnice(1, 2, 5))   # Očekávaný výstup: None