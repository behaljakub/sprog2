def rle(lst):
    if not lst:
        return []
    
    vysledek = []
    count = 1

    for x in range(1, len(lst)):
        if lst[x] == lst[x-1]:
            count += 1
        else:
            vysledek.append([lst[x-1], count])
            count = 1

    vysledek.append([lst[-1], count])
    return vysledek

print(rle([1, 1, 1, 2, 2, 3]))   # → [[1, 3], [2, 2], [3, 1]]
print(rle([1, 1, 2, 1, 1]))       # → [[1, 2], [2, 1], [1, 2]]
print(rle([]))                    # → []



