import random
import copy
import random
from bubble_sort import bubble_v1
from bubble_sort import bubble_v2
from bubble_sort import bubble_v3
from bubble_sort import bubble_v4
from insert_sort import insertion_sort
from selection_sort import selection_sort


def measure_sorts():
    lists_lens = [x for x in range(10, 50, 10)]
    bubble_v1_res = []
    bubble_v2_res = []
    bubble_v3_res = []
    bubble_v4_res = []
    insertion_sort_res = []
    selection_sort_res = []

    for x in range(10, 50, 10):
        unsorted_list = [random.randint(0, x**2) for i in range(x)]

        bubble_v1_res.append(bubble_v1(copy.deepcopy(unsorted_list)))

        bubble_v2_res.append(bubble_v2(copy.deepcopy(unsorted_list)))

        bubble_v3_res.append(bubble_v3(copy.deepcopy(unsorted_list)))

        bubble_v4_res.append(bubble_v4(copy.deepcopy(unsorted_list)))

        insertion_sort_res.append(insertion_sort(copy.deepcopy(unsorted_list)))

        selection_sort_res.append(selection_sort(copy.deepcopy(unsorted_list)))

measure_sorts()