def partition(left, right, seznam):
    count = 0
    pivot_index = (left + right)//2
    pivot = seznam[pivot_index]
    i = left
    j = right
    while j >= i:
        while seznam[i] < pivot:
            count += 1
            i +=1
        while seznam[j] > pivot:
            count += 1
            j -= 1
        count += 1

        if i <= j:
            temp = seznam[i]
            seznam[i] = seznam[j]
            seznam[j] = temp
            i += 1
            j-= 1
            count += 1

    return i, count
    

def quick_sort(left, right, seznam):
    count = 0
    if left < right:
        i, c = partition(left, right, seznam)
        count += c
        count_right = quick_sort(i, right, seznam)
        count_left = quick_sort(left, i - 1, seznam)
        count += count_left + count_right        
    return count


seznam2 = [8, 2, 7, 1452, 4, 5, 3, 465, 2, 6, 1, 4, 24, 55, 4, 1, 124, 562, 2]

print(quick_sort(0, len(seznam2) - 1, seznam2))

