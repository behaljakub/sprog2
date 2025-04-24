def vypis_suda_od_do(zacatek, konec):
    if zacatek < konec:
        for i in range(zacatek, konec + 1):
            if i%2 == 0:
                print(i)
    

vysledek = vypis_suda_od_do(4, 12)


