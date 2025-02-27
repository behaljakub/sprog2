l = [2, 3, 1, 0, 5, 6, 4, 2]  # Seznam čísel
target = int(input("Zadej číslo, které chceš najít: "))  # Uživatelský vstup
misto = []  # Seznam pro indexy
index = 0  # Počáteční index

for i in l:  # Procházení seznamu
    if i == target:  # Pokud je prvek rovný hledanému číslu
        misto.append(index)  # Přidáme jeho index do seznamu
    index += 1  # Posuneme index o 1

print("Číslo", target, "se nachází na indexech:", misto)