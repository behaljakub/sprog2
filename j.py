import random

# Načtení délky seznamu od uživatele
delka = int(input("Zadej délku seznamu: "))

# Vytvoření prázdného seznamu
cisla = []

# Naplnění seznamu náhodnými čísly
for i in range(delka):
    cislo = random.randint(1, 10)
    cisla.append(cislo)

# Výstup seznamu
print("Vygenerovaný seznam:", cisla)

target = int(input("Zadejte cislo k hledání: "))
index = 0
retezec = []

for x in cisla:
    if x == target:
        retezec.append(index)
    index += 1

print(f"Cislo {target} se nachází na indexech {retezec}")

