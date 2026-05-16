def do_dvojkove(n):
    cislo = ""
    while n > 0:
        vysledek = n%2
        n//2
        cislo = vysledek + cislo
    return cislo


print(do_dvojkove(5))    # → '101'
print(do_dvojkove(10))   # → '1010'
print(do_dvojkove(255))  # → '11111111'
