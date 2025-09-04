def NSD(cislo, cislo2):
    zbytek = cislo%cislo2

    if zbytek == 0:
        return cislo2
    
    else:
        return NSD(cislo2, zbytek)
    
print(NSD(15,20))