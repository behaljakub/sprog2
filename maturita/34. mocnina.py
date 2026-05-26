def mocnina(x, n):
    if n == 0:
        return 1
    
    return x*mocnina(x, n-1)

print(mocnina(2, 0))    # → 1
print(mocnina(2, 10))   # → 1024
print(mocnina(3, 4))    # → 81