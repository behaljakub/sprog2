import random

delka = int(input("Zadej délku seznamu: "))

cisla = []
for i in range(delka):
    cislo = random.randint(1, 100)
    cisla.append(cislo)

print("Vygenerovaný seznam:", cisla)

dolnihranice = int(input("Zadej dolní hranici intervalu: "))
hornihranice = int(input("Zadej horní hranici intervalu: "))

count = 0
for cislo in cisla:
    if dolnihranice <= cislo <= hornihranice:
        count += 1

print(f"Počet čísel v intervalu [{dolnihranice}, {hornihranice}] je: {count}")