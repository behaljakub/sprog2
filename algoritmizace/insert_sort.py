import random
import copy
import time

def insertion_sort(seznam):
    for x in range(1, len(seznam)):
        key = seznam[x]
        j = x - 1
        while j >= 0 and seznam[j] > key:
            seznam[j + 1] = seznam[j]
            j -= 1
        seznam[j + 1] = key
    return seznam

print(insertion_sort([5, 5, 4, 1, 2]))



