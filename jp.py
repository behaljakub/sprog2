def ciferny_soucet(n):

    n = abs(n)
    soucet = 0
    for x in str(n):
        soucet += n%10
        n//10
    return soucet

print(ciferny_soucet(55))
print(ciferny_soucet(123))