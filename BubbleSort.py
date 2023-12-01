def BubbleSort(arr):
    for i in range (len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                Swap(arr, j, j+1)
    return arr

def Swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


list = [2,8,5,3,9,4,1]

print(BubbleSort(list))