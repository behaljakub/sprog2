def bubble_v3(n):
    delka = len(n)
    count = 0
    for i in range(delka - 1):
        for j in range(delka - 1 - i):
            count += 1
            if n[j] > n[j + 1]:
                temp = n[j]
                n[j] = n[j+1]
                n[j+1] = temp
    
    return count