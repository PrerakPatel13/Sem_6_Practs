import random
import time

def partition_hoare(a, low, high):
    p_index = random.randint(low, high)
    a[p_index], a[high] = a[high], a[p_index]
    pivot = a[high]
    i = low - 1
    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1

def hoare(a, low, high):
    i = random.randint(low, high)
    j = random.randint(low, high)
    while i >= j:
        i = random.randint(low, high)
        j = random.randint(low, high)
    a[i], a[j] = a[j], a[i]
    return partition_hoare(a, low, high)

def quicksort(a, low, high, partition_func):
    if low < high:
        p = partition_func(a, low, high)
        quicksort(a, low, p - 1, partition_func)
        quicksort(a, p + 1, high, partition_func)

file_name = 'inputhoare.txt'
with open(file_name, 'w') as file:
    for _ in range(100000):
        file.write(str(random.randint(1, 1000000)) + '\n')
with open(file_name, 'r') as file:
    a = list(map(int, file.read().split()))

n = len(a)

a_copy = a.copy()
print("\nHoare Partition:")
start_time = time.time()
quicksort(a_copy, 0, n - 1, hoare)
end_time = time.time()
print(f"Sorted Array: {a_copy}")  
print(f"Time taken: {end_time - start_time} seconds")
