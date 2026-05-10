def fak(n):
    vysledek = 1
    for x in range(1, n + 1):
        vysledek*=x

    return vysledek

print(fak(5))   # Očekávaný výstup: 120
print(fak(3))   # Očekávaný výstup: 6
print(fak(0))   # Očekávaný výstup: 1
