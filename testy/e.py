def konvertor_men(castka, z_meny, na_menu, kurzy=None):
    vychozi_kurzy = {
    "CZK": 1.0,
    "EUR": 0.04,
    "USD": 0.043,
    "GBP": 0.034,
    "JPY": 6.43
    }
    
    if kurzy == None:
        kurzy = vychozi_kurzy
    
    if castka <= 0 or z_meny not in vychozi_kurzy or na_menu not in vychozi_kurzy:
        return None
    
    prvni_prevod = castka/kurzy[z_meny]
    druhy_prevod = prvni_prevod*kurzy[na_menu]


    vysledek = round(druhy_prevod, 2)

    return vysledek

print(konvertor_men(1000, "CZK", "EUR"))  # 40.0
print(konvertor_men(50, "EUR", "CZK"))  # 1250.0
print(konvertor_men(100, "USD", "JPY"))  # 14953.49
print(konvertor_men(75, "GBP", "USD", {"GBP": 1.00, "USD": 1.26}))  # 94.5
print(konvertor_men(200, "CZK", "XYZ"))  # None








