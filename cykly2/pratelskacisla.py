for number in range(1, 10000):
    soucet1 = 0
    soucet2 = 0
    for i in range(1, number):
        if number % i == 0:
            soucet1 += i
    for i in range(1, soucet1):
        if soucet1%i == 0:
            soucet2 += i

    if number == soucet2 and number != soucet1:
        print(f"{number} - {soucet1} jsou přátelská čísla")