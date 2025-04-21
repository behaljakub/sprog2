def je_prvocislo(n):
    if n < 2:
        return False
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return True

cisla = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prvocisla = [n for n in cisla if je_prvocislo(n)]
print(prvocisla)