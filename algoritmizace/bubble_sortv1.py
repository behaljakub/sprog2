def bubble_v1(n):
    count = 0
    for x in range(0, len(n)):
        for y in range(len(n) - 1):
            count += 1
            if n[y] > n[y+1]:
                temp = n[y]
                n[y] = n[y+1]
                n[y+1] = temp
    return count



