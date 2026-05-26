def slouceni_setrizene(a, b):
    vysledek = []

    for x in a:
        vysledek.append(x)

    for y in b:
        vysledek.append(y)


    for x in range(0, len(vysledek)):
        for y in range(len(vysledek) - 1):
            if vysledek[y] > vysledek[y+1]:
                vysledek[y], vysledek[y+1] = vysledek[y+1], vysledek[y]

    return vysledek


print(slouceni_setrizene([1, 3, 5], [2, 4, 6]))   # → [1, 2, 3, 4, 5, 6]