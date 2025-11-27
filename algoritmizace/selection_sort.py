def selection_sort(n):
    steps = 0
    for x in range(0, len(n)):
        min_index = x
        for i in range(x + 1, len(n)):
            steps += 1
            if n[i] < n[min_index]:
                min_index = i
        n[x], n[min_index] = n[min_index], n[x]


    return steps








