def bubble_v4(n):
    start = 0 
    end =  len(n) - 1
    count = 0

    for z in range(1000):
        swapped = False
        for x in range(start, end):
            if n[x] > n[x+1]:
                temp = n[x]
                n[x] = n[x+1]
                n[x+1] = temp
                swapped = True
                count += 1
        if not swapped:
            break
        end -= 1

        swapped = False
        for i in range(end, start, -1):
            if n[i] < n[i - 1]:
                temp = n[i]
                n[i] = n[i+1]
                n[i+1] = temp
                swapped = True
                count += 1
        start += 1
        
        if not swapped:
            break

    return count