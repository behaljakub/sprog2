cislo = int(input("Zadejte číslo: "))

vysledek = 1

for x in range(1, cislo + 1):
    	vysledek*= x

print(f"Faktoriál čísla {cislo} je {vysledek}")