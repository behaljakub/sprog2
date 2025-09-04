x_souradnice = [1, 2, 3]
y_souradnice = [2, 4, 6]


def costf(k):
    sum = 0
    for i in range(len(x_souradnice)):
        sum += (y_souradnice[i] - k*x_souradnice[i])**2
    return 1/len(x_souradnice) * sum

for i in range(-5, 6, 1):
    print(f"k: {i}, Cost func. je: {costf(i)}")

    



