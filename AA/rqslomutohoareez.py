import random
import time

def hoare_partition(arr, low, high, pivot_strategy):
    if pivot_strategy == 'hoare_random':
        pivot_index = random.randint(low, high)
        arr[pivot_index], arr[low] = arr[low], arr[pivot_index]
    pivot = arr[low]
    i = low - 1
    j = high + 1
    
    while True:
        while True:
            i += 1
            if arr[i] >= pivot:
                break       
        while True:
            j -= 1
            if arr[j] <= pivot:
                break       
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]

def lumoto_partition(arr, low, high, pivot_strategy):
    if pivot_strategy == 'lumoto_random':
        pivot_index = random.randint(low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high, pivot_strategy):
    if low < high:
        if pivot_strategy in ['lumoto_base', 'lumoto_random']:
            pivot_index = lumoto_partition(arr, low, high, pivot_strategy)
        else:
            pivot_index = hoare_partition(arr, low, high, pivot_strategy)
        
        quicksort(arr, low, pivot_index - 1, pivot_strategy)
        quicksort(arr, pivot_index + 1, high, pivot_strategy)

array_size = 990
random_array = [random.randint(0, 1000) for _ in range(array_size)]
random_array1 = random_array.copy()
random_array2 = random_array.copy()
random_array3 = random_array.copy()

start_time = time.time()
quicksort(random_array, 0, len(random_array) - 1, 'lumoto_base')
end_time = time.time()
print(f"LUMOTO BASE: {(end_time-start_time)*1000:.3f} ms")
print("Array after LUMOTO BASE sorting:", random_array[:10])

start_time = time.time()
quicksort(random_array1, 0, len(random_array1) - 1, 'lumoto_random')
end_time = time.time()
print(f"LUMOTO RANDOM: {(end_time-start_time)*1000:.3f} ms")
print("Array after LUMOTO RANDOM sorting:", random_array1[:10])

start_time = time.time()
quicksort(random_array2, 0, len(random_array2) - 1, 'hoare_base')
end_time = time.time()
print(f"HOARE BASE: {(end_time-start_time)*1000:.3f} ms")
print("Array after HOARE BASE sorting:", random_array2[:10])

start_time = time.time()
quicksort(random_array3, 0, len(random_array3) - 1, 'hoare_random')
end_time = time.time()
print(f"HOARE RANDOM: {(end_time-start_time)*1000:.3f} ms")
print("Array after HOARE RANDOM sorting:", random_array3[:10])
