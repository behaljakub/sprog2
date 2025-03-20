pocet = int(input("Zadejte počet studentů: "))

hodnoceni = {}

for x in range(pocet):
    jmeno = input("Jmeno studenta: ")
    pocet_znamek = int(input("Pocet znamek: "))
    znamky = []
    for j in range(pocet_znamek):
        znamka = input("Zadejte znamku: ")
        znamky.append(znamka)

    hodnoceni[jmeno] = znamky

for klic, hodnota in hodnoceni.items():
    prumer  = sum(hodnota) / len(hodnota)
    
    print(f"{klic} - {hodnota}")