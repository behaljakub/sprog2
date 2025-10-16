def partition(left, right, seznam):
    pivot_index = (left + right)//2
    pivot = seznam[pivot_index]
    i = left
    j = right
    while j >= i:
        while seznam[i] < pivot:
            i +=1
        while seznam[j] > pivot:
            j -= 1

        if i <= j:
            temp = seznam[i]
            seznam[i] = seznam[j]
            seznam[j] = temp
            i += 1
            j-= 1

    return i
    

def quick_sort(left, right, seznam):
    if left < right:
        i = partition(left, right, seznam)
        quick_sort(i, right, seznam)
        quick_sort(left, i - 1, seznam)
        
    return seznam


seznam2 = [8, 2, 7, 1452, 4, 5, 3, 465, 2, 6, 1, 4, 24, 55, 4, 1, 124, 562, 2]

print(quick_sort(0, len(seznam2) - 1, seznam2))

