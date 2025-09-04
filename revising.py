seznam =  [5, 3, 1, 2, 6]

for x in range(0, len(seznam)):
    for y in range(len(seznam) - 1):
        if seznam[y] > seznam[y+1]:
            temp = seznam[y]
            seznam[y] = seznam[y+1]
            seznam[y+1] = temp
            print(seznam)
            