def shell_sort(seznam):
    count = 0
    mezera = len(seznam) // 2
    while mezera > 0:
        for x in range(mezera, len(seznam)):
            temp = seznam[x]
            j = x
            while j >= mezera and seznam[j - mezera] > temp:
                seznam[j] = seznam[j - mezera]
                j -= mezera
                count += 1
            seznam[j] = temp
        mezera //= 2
    return count
