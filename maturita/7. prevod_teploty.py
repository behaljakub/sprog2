def teplota_c(n):
    f=(9/5)*n + 32
    k=n+273.15

    return f"Kelviny {k} K, Fahrenheit: {f} F"

# Vstup:  0
# Výstup: Kelviny: 273.15 K, Fahrenheity: 32.00 °F

# Vstup:  25
# Výstup: Kelviny: 298.15 K, Fahrenheity: 77.00 °F

# Vstup:  100
# Výstup: Kelviny: 373.15 K, Fahrenheity: 212.00 °F

print(teplota_c(0))
print(teplota_c(25))
print(teplota_c(100))