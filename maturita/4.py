def eratosthenovo_sito(n):
    seznam = []
    for x in range(2, n + 1):
        seznam.append(x)

    
    for i in seznam:
        for k in range(i*2, n+1, i):
            if k in seznam:
                seznam.remove(k)
    return seznam
print(eratosthenovo_sito(10))