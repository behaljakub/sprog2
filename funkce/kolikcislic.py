def pocet_cislic(n):
    n = abs(n)
    return len(str(n))

print(pocet_cislic(12345))
print(pocet_cislic(-27))
print(pocet_cislic(0))


