def bubble_v2(n):
    count2 = 0
    for x in range(len(n) - 1):
        swapped = False
        for y in range(len(n) - 1):
            if n[y] > n[y+1]:
                temp = n[y]
                n[y] = n[y+1]
                n[y+1] = temp
                swapped = True
                count2 += 1
        if not swapped:
            break
    return count2