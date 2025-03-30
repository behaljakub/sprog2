text = str(input("Zadejte text: "))
pocet = {}

pomoci_seznam = text.split()

for slovo in pomoci_seznam:
    if slovo in pocet.keys():
        pocet[slovo] += 1
    else:
        pocet[slovo] = 1

for klic, hodnota in pocet.items():
    print(f"{klic} - {hodnota}")