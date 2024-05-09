import random
import time

def partition_lomuto(a, low, high):
    p_index = random.randint(low, high)
    a[p_index], a[high] = a[high], a[p_index]
    pivot = a[high]
    i = low
    for j in range(low, high):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[high] = a[high], a[i]
    return i

def lomuto(a, low, high):
    i = random.randint(low, high)
    j = random.randint(low, high)
    while i >= j:
        i = random.randint(low, high)
        j = random.randint(low, high)
    a[i], a[j] = a[j], a[i]
    return partition_lomuto(a, low, high)

def quicksort(a, low, high, partition_func):
    if low < high:
        p = partition_func(a, low, high)
        quicksort(a, low, p - 1, partition_func)
        quicksort(a, p + 1, high, partition_func)

file_name = 'input_lomuto.txt'
with open(file_name, 'w') as file:
    for _ in range(100000):
        file.write(str(random.randint(1, 1000000)) + '\n')
with open(file_name, 'r') as file:
    a = list(map(int, file.read().split()))

n = len(a)

a_copy = a.copy()
print("\nLomuto Partition:")
start_time = time.time()
quicksort(a_copy, 0, n - 1, lomuto)
end_time = time.time()
print(f"Sorted Array: {a_copy}")  
print(f"Time taken: {end_time - start_time} seconds")
