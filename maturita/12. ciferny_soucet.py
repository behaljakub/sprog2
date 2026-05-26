def ciferny_soucet(n):
    n = str(n)
    soucet = 0
    for x in n:
        soucet += int(x)
    return soucet

print(ciferny_soucet(123))    # → 6
print(ciferny_soucet(999))    # → 27
print(ciferny_soucet(0))      # → 0
print(ciferny_soucet(1000))   # → 1
    