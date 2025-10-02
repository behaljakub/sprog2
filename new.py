import matplotlib.pyplot as plt
import random

# Funkce řadící algoritmy
def bubble_v1(n):
    count = 0
    for x in range(0, len(n)):
        for y in range(len(n) - 1):
            count += 1
            if n[y] > n[y+1]:
                n[y], n[y+1] = n[y+1], n[y]
    return count

def bubble_v2(n):
    count2 = 0
    for x in range(len(n) - 1):
        swapped = False
        for y in range(len(n) - 1):
            if n[y] > n[y+1]:
                n[y], n[y+1] = n[y+1], n[y]
                swapped = True
                count2 += 1
        if not swapped:
            break
    return count2

def bubble_v3(pole):
    n = len(pole)
    count = 0
    for i in range(n - 1):
        for j in range(n - 1 - i):
            count += 1
            if pole[j] > pole[j + 1]:
                pole[j], pole[j + 1] = pole[j + 1], pole[j]
    return count

def bubble_v4(n):
    start = 0 
    end =  len(n) - 1
    count = 0
    for z in range(1000):
        swapped = False
        for x in range(start, end):
            if n[x] > n[x+1]:
                n[x], n[x + 1] = n[x + 1], n[x]
                swapped = True
                count += 1
        if not swapped:
            break
        end -= 1

        swapped = False
        for i in range(end, start, -1):
            if n[i] < n[i - 1]:
                n[i], n[i - 1] = n[i-1], n[i]
                swapped = True
                count += 1
        start += 1
        if not swapped:
            break
    return count

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

def selection_sort(n):
    count = 0
    for x in range(0, len(n)):
        min_index = x
        for i in range(x + 1, len(n)):
            count +=1
            if n[i] < n[min_index]:
                min_index = i
        n[x], n[min_index] = n[min_index], n[x]
    return count

# Velikosti vstupů
sizes = [10, 20, 30, 40, 50, 100, 200]
results = {
    "bubble_v1": [],
    "bubble_v2": [],
    "bubble_v3": [],
    "bubble_v4": [],
    "insertion_sort": [],
    "selection_sort": []
}

# Simulace a měření
for size in sizes:
    data = [random.randint(0, 1000) for _ in range(size)]
    results["bubble_v1"].append(bubble_v1(data.copy()))
    results["bubble_v2"].append(bubble_v2(data.copy()))
    results["bubble_v3"].append(bubble_v3(data.copy()))
    results["bubble_v4"].append(bubble_v4(data.copy()))
    results["insertion_sort"].append(insertion_sort(data.copy()))
    results["selection_sort"].append(selection_sort(data.copy()))

# Vykreslení grafu
plt.figure(figsize=(12, 6))
for algo, counts in results.items():
    plt.plot(sizes, counts, marker='o', label=algo)

plt.title("Počet výměn/porovnání vs Velikost vstupu")
plt.xlabel("Velikost vstupu")
plt.ylabel("Počet výměn/porovnání")
plt.legend()
plt.grid(True)
plt.show()
