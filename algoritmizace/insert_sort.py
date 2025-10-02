import random
import copy
import time

def insertion_sort(seznam):
    steps = 0
    for x in range(1, len(seznam)):
        key = seznam[x]
        j = x - 1
        while j >= 0 and seznam[j] > key:
            steps += 1
            seznam[j + 1] = seznam[j]
            j -= 1
        seznam[j + 1] = key
    return steps



def measure_sorts():
    unsorted_list = []
    for i in range(1000):
        x = random.randint(0, 100)
        unsorted_list.append(x)
    list_copy = copy.deepcopy(unsorted_list)

    time_start = time.perf_counter()
    comparisons = insertion_sort(list_copy)
    time_end = time.perf_counter()

    execution_time = time_end - time_start

    print(f"InsertionSort - pocet porovnani: {comparisons}, cas: {execution_time}")
