   
def quick_sort(seznam):
    count = 0
    def partition(left, right, seznam):
        nonlocal count
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

        return i
    

    def _quick_sort(left, right, seznam):
        nonlocal count
        if left < right:
            i = partition(left, right, seznam)
            _quick_sort(i, right, seznam)
            _quick_sort(left, i - 1, seznam)
    _quick_sort(0, len(seznam) - 1, seznam)
    return count

