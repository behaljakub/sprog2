kurzy = {"USD": 22.5,"EUR": 24.5,  "GBP": 28.0}

mena = input("Zadejte kód měny (USD, EUR, GBP): ").upper()
castka = float(input("Zadejte částku v měně: "))

if mena in kurzy:
    ekvivalent = castka * kurzy[mena]
    print(f"{castka} {mena} je {ekvivalent:.2f} CZK.")
else:
    print("Měna není ve slovníku.")

