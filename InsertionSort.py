def InsertionSort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            swap(arr, j, j-1)
            j -= 1
    return arr

def swap(arr, i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


list = [2,8,5,3,9,4,1]
print(InsertionSort(list))