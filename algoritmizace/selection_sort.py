def selection_sort(n):
    for x in range(0, len(n)):
        min_index = x
        for i in range(x + 1, len(n)):
            if n[i] < n[min_index]:
                min_index = i
        n[x], n[min_index] = n[min_index], n[x]

    return n

seznam = [5, 1, 4, 2, 7, 3]

print(selection_sort(seznam))

