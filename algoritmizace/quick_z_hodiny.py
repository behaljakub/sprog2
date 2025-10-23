count = 0

def partition(left, right, pivot, numbers):

    while (left <= right):
        global count
        count += 1
        while numbers[left] < pivot:
            left += 1

        while numbers[right] > pivot:
            right -= 1

        if left <= right:
            temp = numbers[left]
            numbers[left] = numbers[right]
            numbers[right] = temp

            left += 1
            right -= 1

    return left


def quick_sort(left, right, numbers):
    global count
    count += 1
    if left < right:
        pivot = numbers[(left + right) // 2]
        mid = partition(left, right, pivot, numbers)
        quick_sort(left, mid - 1, numbers)
        quick_sort(mid, right, numbers)

numbers = [5, 5, 5]
left = 0
right = len(numbers) - 1
print(numbers)
quick_sort(left, right, numbers)
print(numbers)
print(count)
