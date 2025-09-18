seznam = [23, 1, 10, 5, 2]

for x in range(1):
    if seznam[x+1] < seznam[x]:
        temp = seznam[x]
        seznam[x] = seznam[x+1]
        seznam[x+1] = temp
        for i in range(1):
            if seznam[i+2] < seznam[i+1]:
                temp1 = seznam[i+1]
                seznam[i+1] = seznam[i+2]
                seznam[i+2] = temp1
print(seznam)


