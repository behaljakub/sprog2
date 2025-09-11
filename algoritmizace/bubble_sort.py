import copy
import random
import time

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

def bubble_v2(n):
    count2 = 0
    for x in range(0, len(n)):
        swapped = False
        for y in range(len(n) - 1):
            if n[y] > n[y+1]:
                temp = n[y]
                n[y] = n[y+1]
                n[y+1] = temp
                swapped = True
                count2 += 1
        if not swapped:
            swapped = False
    return count2

def bubble_v3(n):
    count3 = 0 
    swapped = False
    for x in range(0, len(n) - 1):
        end = len(n) - 1
        if x == end - 1:
            if n[x] <= n[x+1]:
                end -= 1
                break 
        count3 += 1
        for y in range(0, len(n) - 1):
            if n[y] > n[y+1]:
                temp = n[y]
                n[y] = n[y+1]
                n[y+1] = temp
                swapped = True
        
    if not swapped:
        swapped = False

    return count3
def bubble_v4(n):
    start = 0 
    end =  len(n) - 1
    count = 0

    for z in range(10000):
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
                temp2 = n[i]
                n[i] = n[i-1]
                n[i-1] = temp2
                swapped = True
                count += 1
        if not swapped:
            break
        start += 1

    return count

def measure_sorts():
    unsorted_list = []
    for i in range(1000):
        x = random.randint(0, 100)
        unsorted_list.append(x)
    list_copy = copy.deepcopy(unsorted_list)

    time_start = time.perf_counter()
    comparisons = bubble_v1(list_copy)
    time_end = time.perf_counter()

    execution_time = time_end - time_start

    print(f"Bubble v1 - pocet porovnani: {comparisons}, cas: {execution_time}")


    list_copy = copy.deepcopy(unsorted_list)

    time_start = time.perf_counter()
    comparisons = bubble_v2(list_copy)
    time_end = time.perf_counter()

    execution_time = time_end - time_start

    print(f"Bubble v2 - pocet porovnani: {comparisons}, cas: {execution_time}")

    list_copy = copy.deepcopy(unsorted_list)

    time_start = time.perf_counter()
    comparisons = bubble_v3(list_copy)
    time_end = time.perf_counter()

    execution_time = time_end - time_start

    print(f"Bubble v3 - pocet porovnani: {comparisons}, cas: {execution_time}")

    list_copy = copy.deepcopy(unsorted_list)

    time_start = time.perf_counter()
    comparisons = bubble_v4(list_copy)
    time_end = time.perf_counter()

    execution_time = time_end - time_start

    print(f"Bubble v4 - pocet porovnani: {comparisons}, cas: {execution_time}")

measure_sorts()


