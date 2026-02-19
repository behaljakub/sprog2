def sito(n):
    seznam = []
    for x in range(2, n + 1):
        seznam.append(x)


    for i in seznam:
        for j in range(i*2, n + 1, i):
            if j in seznam:
                seznam.remove(j)
    
    return seznam
    

print(sito(20))