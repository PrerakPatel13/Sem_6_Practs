import random
import time

def lumoto_base(arr,low,high):
    if low<high:
        start = low - 1
        pivot = high
        for end in range(low,high):
            if arr[end] <= arr[pivot]:
                start+=1
                arr[start],arr[end] = arr[end],arr[start]
        arr[start+1],arr[high] = arr[high],arr[start+1]
        p = start+1
        lumoto_base(arr,low,p-1)
        lumoto_base(arr,p+1,high)


def lumoto_random(arr,low,high):
    if low<high:
        start = low - 1
        k = random.randint(low,high)
        arr[k],arr[high] = arr[high],arr[k]
        pivot = high
        for end in range(low,high):
            if arr[end] <= arr[pivot]:
                start+=1
                arr[start],arr[end] = arr[end],arr[start]
        arr[start+1],arr[high] = arr[high],arr[start+1]
        p = start+1
        lumoto_base(arr,low,p-1)
        lumoto_base(arr,p+1,high)        

def hoare_base(arr,low,high):
    if low<high:
        start = low
        end = high
        pivot = low
        while start<end:
            while arr[start]<=arr[pivot] and start<high:
                start+=1
            while arr[end]>arr[pivot]:
                end-=1
            if start<end:
                arr[start],arr[end] = arr[end],arr[start]
        arr[end],arr[pivot] = arr[pivot],arr[end]
        hoare_base(arr,low,end-1)
        hoare_base(arr,end+1,high)

def hoare_random(arr,low,high):
    if low<high:
        start = low
        end = high
        k = random.randint(low,high)
        arr[k],arr[low] = arr[low],arr[k]
        pivot = low
        while start<end:
            while arr[start]<=arr[pivot] and start<high:
                start+=1
            while arr[end]>arr[pivot]:
                end-=1
            if start<end:
                arr[start],arr[end] = arr[end],arr[start]
        arr[end],arr[pivot] = arr[pivot],arr[end]
        hoare_random(arr,low,end-1)
        hoare_random(arr,end+1,high)
 
array_size = 990
random_array = [random.randint(0, 1000) for _ in range(array_size)]
random_array1 = random_array.copy()
random_array2 = random_array.copy()
random_array3 = random_array.copy()

start_time = time.time()
lumoto_base(random_array, 0, len(random_array) - 1)
end_time = time.time()
print(f"LUMOTO BASE: {(end_time-start_time)*1000}")

start_time = time.time()
lumoto_random(random_array1 ,0, len(random_array) - 1)
end_time = time.time()
print(f"LUMOTO RANDOM: {(end_time-start_time)*1000}")

start_time = time.time()
hoare_base(random_array2, 0, len(random_array) - 1)
end_time = time.time()
print(f"HOARE BASE: {(end_time-start_time)*1000}")

start_time = time.time()
hoare_random(random_array3, 0, len(random_array) - 1)
end_time = time.time()
print(f"HOARE RANDOM: {(end_time-start_time)*1000}")