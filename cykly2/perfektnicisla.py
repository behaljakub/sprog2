for x in range(2, 1000):
    temp_sum = 0
    for i in range(1, x):
        if x % i == 0:
            temp_sum += i
    if x == temp_sum:
        print(f"{x} je perfektní")


