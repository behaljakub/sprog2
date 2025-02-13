cislo = [2, 3, 1, 0, 5, 6, 4, 9]

maxn = cislo[0]
minn = cislo[0]

for i in cislo:
    if i > maxn:
        maxn = i

print(maxn)

for n in cislo:
    if n < minn:
        minn = n 

print(minn)

soucet = 0

for k in cislo:
    soucet += k



print(soucet/len(cislo))


    



