seznam =  [5, 3, 1, 2, 6]

for x in range(len(seznam) - 1):
    for y in range(x):
        if seznam[x] > seznam[x+1]:
            temp = seznam[x]
            seznam[x] = seznam[x+1]
            temp = seznam[x+1]
            print(seznam)
            