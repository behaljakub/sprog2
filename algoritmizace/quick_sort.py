def partition(left, right, seznam, count):
    pivot_index = (left + right) // 2
    pivot = seznam[pivot_index]
    i = left
    j = right

    while i <= j:
        while seznam[i] < pivot:
            count += 1
            i += 1
        count += 1  

        while seznam[j] > pivot:
            count += 1
            j -= 1
        count += 1  

        if i <= j:
            seznam[i], seznam[j] = seznam[j], seznam[i]
            i += 1
            j -= 1
    return i, count


def _quick_sort(left, right, seznam, count):
    if left < right:
        i, count = partition(left, right, seznam, count)
        count = _quick_sort(left, i - 1, seznam, count)
        count = _quick_sort(i, right, seznam, count)
    return count


def quick_sort(seznam):
    if len(seznam) <= 1:
        return 0
    return _quick_sort(0, len(seznam) - 1, seznam, 0)


