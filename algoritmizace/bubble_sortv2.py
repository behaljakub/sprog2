def bubble_v3(n):
    count3 = 0 
    swapped = False
    for x in range(0, len(n) - 1):
        end = len(n) - 1
        if x == end - 1:
            if n[x] <= n[x+1]:
                end -= 1
                break 
        for y in range(0, len(n) - 1):
            count3 += 1
            if n[y] > n[y+1]:
                temp = n[y]
                n[y] = n[y+1]
                n[y+1] = temp
                swapped = True
        
    if not swapped:
        swapped = False

    return n, count3
seznam = [5, 1, 6, 2, 4]
print(bubble_v3(seznam))