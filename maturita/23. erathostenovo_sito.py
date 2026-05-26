def eratosthenovo_sito(n):
    cisla = []
    for x in range(2, n+1):
        cisla.append(x)

    
    for i in cisla:
        for z in range(i*2, n+1, i):
            if z in cisla:
                cisla.remove(z)

    return cisla

print(eratosthenovo_sito(10))   # → [2, 3, 5, 7]
print(eratosthenovo_sito(20))   # → [2, 3, 5, 7, 11, 13, 17, 19]
print(eratosthenovo_sito(1))    # → []

