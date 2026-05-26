def vzd(s, h, m):
    hodina = h*60
    minuta = hodina + m
    hodina = minuta/60
    prumer_rych = s/(hodina)
    

    return prumer_rych

print(vzd(150, 2, 30))
