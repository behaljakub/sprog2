

def slouceni_bez_duplicit(a, b):
    vysledek = []

    for prvek in a:
        if prvek not in vysledek:
            vysledek.append(prvek)

    for prvek in b:
        if prvek not in vysledek:
            vysledek.append(prvek)

    return vysledek


print(slouceni_bez_duplicit([1, 2, 3], [2, 3, 4, 5]))   # → [1, 2, 3, 4, 5]
print(slouceni_bez_duplicit([1, 1, 2, 3], [4, 5]))       # → [1, 2, 3, 4, 5]
print(slouceni_bez_duplicit([1, 2, 3], [1, 2, 3]))        # → [1, 2, 3]
    
