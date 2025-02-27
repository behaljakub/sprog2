for number in range(1, 100):
    soucet = 0
    temp_number = number

    while temp_number != 1 or temp_number != 4:
        soucet = 0
        for i in str(number):
            print(f"{temp_number}")
            soucet += int(i)**2
        temp_number = soucet
    if temp_number == 1:
        print()