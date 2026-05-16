def je_prvocislo(n):
    count = 0
    for x in range(1, n+1):
        if n%x == 0:
            count += 1
    
    if count == 2:
        return True
    else:
        return False

print(je_prvocislo(2))    # → True
print(je_prvocislo(17))   # → True
print(je_prvocislo(1))    # → False
print(je_prvocislo(9))    # → False
print(je_prvocislo(97))   # → True