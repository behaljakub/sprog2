text = str(input("Zadejte text: "))
key = int(input("Zadejte posun: "))

abc = ['a', "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "q", "r", "s", "t", "u", "v", "x", "y", "z"]

vysledek = []

for x in range(len(text)):
    pismeno = text[x]
    for y in range(len(abc)):
        if pismeno == abc[y]:
            vysledek += abc[y + key]

print(str(vysledek))




