import random
import copy
import random
from bubble_sortv1 import bubble_v1
from bubble_sortv2 import bubble_v2
from bubble_sortv3 import bubble_v3
from bubble_sortv4 import bubble_v4
from insert_sort import insertion_sort
from selection_sort import selection_sort
from shell_sort import shell_sort
import matplotlib.pyplot as plt


def measure_sorts():
    lists_lens = [x for x in range(10, 100, 10)]
    bubble_v1_res = []
    bubble_v2_res = []
    bubble_v3_res = []
    bubble_v4_res = []
    insertion_sort_res = []
    selection_sort_res = []
    shell_sort_res = []

    for x in range(10, 100, 10):
        unsorted_list = [random.randint(0, x**2) for i in range(x)]

        bubble_v1_res.append(bubble_v1(copy.deepcopy(unsorted_list)))

        bubble_v2_res.append(bubble_v2(copy.deepcopy(unsorted_list)))

        bubble_v3_res.append(bubble_v3(copy.deepcopy(unsorted_list)))

        bubble_v4_res.append(bubble_v4(copy.deepcopy(unsorted_list)))

        insertion_sort_res.append(insertion_sort(copy.deepcopy(unsorted_list)))

        selection_sort_res.append(selection_sort(copy.deepcopy(unsorted_list)))

        shell_sort_res.append(shell_sort(copy.deepcopy(unsorted_list)))



    plt.plot(lists_lens, bubble_v1_res, label = "bubbleV1", color="#FF0000")
    plt.plot(lists_lens, bubble_v2_res, label = "bubbleV2", color="#4400FF")
    plt.plot(lists_lens, bubble_v3_res, label = "bubbleV3", color="#2BFF00")
    plt.plot(lists_lens, bubble_v4_res, label = "bubbleV4", color="#00C3FF")
    plt.plot(lists_lens, insertion_sort_res, label = "insertion", color="#000000")
    plt.plot(lists_lens, selection_sort_res, label = "selection", color="#E100FF")
    plt.plot(lists_lens, shell_sort_res, label = "shell", color="#00AEFF")

    

    


    plt.legend()
    plt.show()

measure_sorts()