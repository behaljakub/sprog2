def najdi_vsechny(lst, hodnota):
    novy = []
    for x in range(len(lst)):
        if lst[x] == hodnota:
            novy.append(x)

    return novy

print(najdi_vsechny([1, 3, 2, 3, 4, 3], 3))   # → [1, 3, 5]
print(najdi_vsechny([1, 2, 3], 5))             # → []
print(najdi_vsechny([7, 7, 7], 7))             # → [0, 1, 2]