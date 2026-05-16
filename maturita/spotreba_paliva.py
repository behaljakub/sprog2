def spotreba(v, s, c):
    palivo = (v/100)*s
    cena = palivo*c

    return palivo, cena

print(spotreba(250, 6, 40))
