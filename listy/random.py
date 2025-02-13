cislo = [2, 3, 1, 0, 5, 6, 4]

maxn = 0
minn = cislo[0]
sum = 0
count = 0

for i in cislo:
    if i > maxn:
        maxn = i
    
    if i < minn:
        minn = i
    
    count += 1
    sum += 1

print(count)



