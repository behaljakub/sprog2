seznam = [2, 8, 9, 1, 3, 4]

for x in seznam:
    for i in range(len(seznam) + 1):

        if seznam[x] > seznam[x+1]:
            seznam[x+1] = seznam[x]
            seznam[x] = seznam[x+1]

print(seznam)


