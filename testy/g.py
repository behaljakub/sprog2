def nejvetsi_spol_del(cislo, cislo2):
    zbytek = cislo%cislo2

    if zbytek == 0:
        return cislo2
    
    else:
        return nejvetsi_spol_del(cislo2, zbytek)
    
print(nejvetsi_spol_del(48, 18))
print(nejvetsi_spol_del(252, 105))
    
