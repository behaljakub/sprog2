cislo = [2, 3, 1, 0, 5, 6, 4]

maxn = 0
minn = 0
sum = 0

for i in range(len(cislo)):
    if maxn > cislo:
        maxn += i
        print(maxn)