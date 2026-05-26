def prvociselny_rozklad(n):
    delitel = 2
    vysledek = []

    while n > 1:
        while n%delitel == 0:
            vysledek.append(str(delitel))
            n//= delitel
        delitel += 1

    return "*".join(vysledek)


print(prvociselny_rozklad(12))    # → '2*2*3'
print(prvociselny_rozklad(28))    # → '2*2*7'
print(prvociselny_rozklad(17))    # → '17'
print(prvociselny_rozklad(100))   # → '2*2*5*5'
    
