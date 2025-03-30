pocet = int(input("Zadejte délku seznam: "))

slovnik = {}

for x in range(pocet):
    jmeno = input("Zadejte jméno: ")
    cislo = input("Zadejte tel. číslo: ")
    slovnik[jmeno] = cislo

for klic, hodnota in slovnik.items():
    print(f"{klic} - {hodnota}")

vyhledavani = str(input("Koho chcete najít: "))
if vyhledavani in slovnik.keys():
    print(slovnik[vyhledavani])
