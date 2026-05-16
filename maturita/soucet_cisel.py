def secti_do_n(n):
    soucet = 0
    for x in range(1, n+1):
        soucet += x
    return soucet
    
print(secti_do_n(5))     # → 15
print(secti_do_n(10))    # → 55
print(secti_do_n(100))   # → 5050
        