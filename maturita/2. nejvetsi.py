def nejvetsi_ze_tri(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
    
print(nejvetsi_ze_tri(15, 8, 12))   # → 15
print(nejvetsi_ze_tri(5, 20, 10))   # → 20
print(nejvetsi_ze_tri(7, 3, 25))    # → 25