import random
import time
import copy
from bubble_sortv1 import bubble_v1
from bubble_sortv2 import bubble_v2
from bubble_sortv3 import bubble_v3
from bubble_sortv4 import bubble_v4

def measure_sorts():
    unsorted_list = []
    for i in range(100):
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