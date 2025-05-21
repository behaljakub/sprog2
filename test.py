def konvertor_men(castka, z_meny, na_menu, kurzy=None):
    # Základní kurzy (vůči 1 CZK)
    vychozi_kurzy = {
        "CZK": 1.0, 
        "EUR": 0.04, #1kc = 0.04 eur
        "USD": 0.043, #1kc = 0.043 eur
        "GBP": 0.034, #1kc = 0.034 gbp
        "JPY": 6.43 #1Kc = 6.43 jpy
        }
    if kurzy == None:
        kurzy = vychozi_kurzy
    
    if castka <= 0 or z_meny not in vychozi_kurzy or na_menu not in vychozi_kurzy:
        return None
    
    prvni_prevod = castka/kurzy[z_meny]
    druhy_prevod = prvni_prevod*kurzy[na_menu]
    vysledek = druhy_prevod
    return round(vysledek, 2)
    
print(konvertor_men(1000, "CZK", "EUR"))  # 40.0
print(konvertor_men(50, "EUR", "CZK"))  # 1250.0
print(konvertor_men(75, "GBP", "USD", {"GBP": 1.26, "USD": 1.0}))  # 94.5
print(konvertor_men(200, "CZK", "XYZ"))  # None

        
    
