import time
import random
import copy
from merge_sort import new_merge
from quick_sort import quick_sort

def measure_sorts():
    unsorted_list = []
    for i in range(1000):
        x = random.randint(0, 100)
        unsorted_list.append(x)

    list_copy = copy.deepcopy(unsorted_list)

    time_start = time.perf_counter()
    comparisons = sorted(list_copy)
    time_end = time.perf_counter()

    execution_time = time_end - time_start

    print(f"Sorted - pocet porovnani: {comparisons}, cas: {execution_time}")

    list_copy = copy.deepcopy(unsorted_list)

    time_start = time.perf_counter()
    comparisons = quick_sort(list_copy)
    time_end = time.perf_counter()

    execution_time = time_end - time_start

    print(f"Merge - pocet porovnani: {comparisons}, cas: {execution_time}")



measure_sorts()