def aritm_posloupnost(a1, d, n):
    for x in range(n):
        print(a1 + x*d, end=" ")

    print()
    
aritm_posloupnost(1, 2, 5)     # → '1 3 5 7 9'
aritm_posloupnost(10, -3, 4)   # → '10 7 4 1'
aritm_posloupnost(0, 5, 3)     # → '0 5 10'