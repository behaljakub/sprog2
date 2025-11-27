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
from quick_sort import quick_sort
from merge_sort import new_merge
import matplotlib.pyplot as plt


def measure_sorts():
    lists_lens = [x for x in range(10, 1000, 200)]
    bubble_v1_res = []
    bubble_v2_res = []
    bubble_v3_res = []
    bubble_v4_res = []
    insertion_sort_res = []
    selection_sort_res = []
    shell_sort_res = []
    quick_sort_res = []
    merge_sort_res = []

    for x in range(10, 1000, 200):
        unsorted_list = [random.randint(0, x**2) for i in range(x)]

        bubble_v1_res.append(bubble_v1(copy.deepcopy(unsorted_list)))

        bubble_v2_res.append(bubble_v2(copy.deepcopy(unsorted_list)))

        bubble_v3_res.append(bubble_v3(copy.deepcopy(unsorted_list)))

        bubble_v4_res.append(bubble_v4(copy.deepcopy(unsorted_list)))

        insertion_sort_res.append(insertion_sort(copy.deepcopy(unsorted_list)))

        selection_sort_res.append(selection_sort(copy.deepcopy(unsorted_list)))
        
        shell_sort_res.append(shell_sort(copy.deepcopy(unsorted_list)))

        quick_sort_res.append(shell_sort(copy.deepcopy(unsorted_list)))

        merge_sort_res.append(shell_sort(copy.deepcopy(unsorted_list)))

        


    #plt.plot(lists_lens, bubble_v1_res, label = "bubbleV1", color="#FF0000")
    #plt.plot(lists_lens, bubble_v2_res, label = "bubbleV2", color="#A200FF")
    #plt.plot(lists_lens, bubble_v3_res, label = "bubbleV3", color="#00FF22")
    #plt.plot(lists_lens, bubble_v4_res, label = "bubbleV4", color="#FFFB00")
    #plt.plot(lists_lens, insertion_sort_res, label = "insertion", color="#0400FF")
    #plt.plot(lists_lens, selection_sort_res, label = "selection", color="#00C3FF")
    #plt.plot(lists_lens, shell_sort_res, label = "shell", color="#00FF9D")
    plt.plot(lists_lens, quick_sort_res, label = "quick", color="#70B1FC")
    plt.plot(lists_lens, merge_sort_res, label = "merge", color="#240086")


    plt.xlabel("Velikost vstupu")
    plt.ylabel("Output")
    plt.legend()
    #plt.yscale("log") #Ověřeni, že ShellSort není konstantní
    plt.show()

measure_sorts()