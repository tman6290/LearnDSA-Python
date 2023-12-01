"""def quickSort(arr):
    qs(arr, 0, len(arr) -1)
    print(arr)

def qs(arr, l , r):
    if l >= r:
        return
    p = partition(arr, l, r)

    qs(arr, l, p-1)
    qs(arr, p+1, r)

def partition(arr, l, r):
    pivot = arr[r]
    i = l -1
    for j in range(l, r):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1

list = [2,4,3,6,5,7,9,38,53]

quickSort(list)"""

# QuickSort by recursion
def QuickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x >= pivot]
        return QuickSort(less) + [pivot] + QuickSort(greater)

    
list = [2,4,3,6,5,7,9,38,53]
print(QuickSort(list))