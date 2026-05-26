def nejvetsi_prvek(lst):
    max = lst[0]
    for x in lst:
        if x > max:
            max = x
    return max

print(nejvetsi_prvek([3, 1, 4, 1, 5, 9, 2, 6]))   # → 9
print(nejvetsi_prvek([-5, -1, -8, -3]))            # → -1
print(nejvetsi_prvek([42]))                        # → 42