import random

list = [random.randint(1, 1000) for _ in range(1000)]


def quick(arr):
    if len(arr) <= 1:
        return arr
    cen = arr[len(arr) // 2]
    mean = sum(arr)/len(arr)
    lef = [x for x in arr if x < mean]
    mid = [x for x in arr if x == mean]
    rig = [x for x in arr if x > mean]
    
    return quick(lef) + mid + quick(rig)
    
print(quick(list))
