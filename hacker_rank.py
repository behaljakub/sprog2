def posloupnost(i):
    seznam = []
    for x in range(1, i + 1):
        seznam.append(x)
    string = "".join(str(cislo) for cislo in seznam)
    print((string))
    
cislo = int(input("Cislo: "))
posloupnost(cislo)

