def soucet(n):
    if n == 1:
        return 1
    
    else:
        return n + soucet(n-1)
    
print(soucet(5))

