def insertion_sort(seznam):
    steps = 0
    for x in range(1, len(seznam)):
        key = seznam[x]
        j = x - 1
        while j >= 0 and seznam[j] > key:
            steps += 1
            seznam[j + 1] = seznam[j]
            j -= 1

        seznam[j + 1] = key
        print(seznam)      
    return seznam, steps

seznam = [7, 6, 1, 4, 2, 9, 8]
print(insertion_sort(seznam))



