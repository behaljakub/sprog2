def kamen_nuzky_papir(hrac1, hrac2):
    if (hrac1 == "kamen" and hrac2 == "nuzky")or (hrac1 == "nuzky" and hrac2 == "papir") or (hrac1 == "papir" and hrac2 == "kamen"):
        return "hrac1"
    elif hrac1 == hrac2:
        return "remiza"
    else:
        return "hrac2"


print(kamen_nuzky_papir('kamen', 'nuzky'))  # → 'hráč 1'
print(kamen_nuzky_papir('papir', 'kamen'))  # → 'hráč 1'
print(kamen_nuzky_papir('kamen', 'kamen'))  # → 'remíza'