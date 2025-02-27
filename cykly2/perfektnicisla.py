for x in range(2, 1000):
    soucet = 0
    for i in range(1, x):
        if x % i == 0:
            soucet += i
    if x == soucet:
        print(f"{x} je perfektní")


