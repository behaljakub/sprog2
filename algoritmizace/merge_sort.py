count = 0

def merge(left, right):
    global count
    spojeno = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        count += 1
        if left[i] < right[j]:
            spojeno.append(left[i])
            i += 1
        else:
            spojeno.append(right[j])
            j += 1
    while i < len(left):
        spojeno.append(left[i])
        i += 1

    while j < len(right):
        spojeno.append(right[j])
        j += 1
    return spojeno

def merge_sort(seznam):
    if len(seznam) <= 1:
         return seznam
    mid = len(seznam)//2
    left = merge_sort(seznam[:mid])
    right = merge_sort(seznam[mid:])
    return merge(left, right)

def new_merge(seznam):
    merge_sort(seznam)
    return count


