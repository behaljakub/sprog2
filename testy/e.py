def konvertor_men(castka, z_meny, na_menu, kurzy=None):
    vychozi_kurzy = {
    "CZK": 1.0, #1 czk = 0.04 eur
    "EUR": 0.04, #1 eur = 0.04 czk
    "USD": 0.043, # 1dol = 0.043 czk
    "GBP": 0.034,
    "JPY": 6.43
    }
    
    if kurzy == None:
        kurzy = vychozi_kurzy
    if z_meny not in kurzy or na_menu not in kurzy or castka < 0:
        return None
    
    castka_ve_stalem_kurzu = castka/kurzy[z_meny]
    vysledna_castka = castka_ve_stalem_kurzu*kurzy[na_menu]
    return round(vysledna_castka, 2)

print(konvertor_men(1000, "CZK", "EUR"))  # 40.0
print(konvertor_men(50, "EUR", "CZK"))  # 1250.0
print(konvertor_men(100, "USD", "JPY"))  # 14953.49
print(konvertor_men(75, "GBP", "USD", {"GBP": 1.26, "USD": 1.0}))  # 94.5 spatne 59.52
print(konvertor_men(200, "CZK", "XYZ"))  # None








