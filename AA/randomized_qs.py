import random
c1,c2 = 0,0
def randomizedqs(arr):
    global c1
    if len(arr) <= 1:
        return arr
    else:
        pivot = random.choice(arr)
        left = []
        right = []
        middle=[]
        for i in range(len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
                c1+=1
            elif arr[i] > pivot:
                right.append(arr[i])
                c1+=1
            else:
                middle.append(pivot)
        return randomizedqs(left) + middle + randomizedqs(right)
def quicksort(arr):
    global c2
    if len(arr)<= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in range(1,len(arr)):
            c2+=1
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quicksort(left) + [pivot] + quicksort(right)        
arr = [random.randint(0, 499) for i in range(500)]
print('Normal Quicksort')
print("Sorted Array:", quicksort(arr))
print("Number of Comparisons:", c2)
print("Randomized QS")
print("Sorted Array:", randomizedqs(arr))
print("Number of Comparisons:", c1)