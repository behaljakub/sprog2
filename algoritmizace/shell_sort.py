def shell_sort(seznam):
    count = 0
    mezera = len(seznam) // 2
    while mezera > 0:
        for i in range(mezera, len(seznam)):
            temp = seznam[i]
            j = i
            while j >= mezera:
                count += 1
                if seznam[j - mezera] > temp:
                    seznam[j] = seznam[j - mezera]
                    j -= mezera
                else:
                    break
            seznam[j] = temp
        mezera //= 2
    return count
