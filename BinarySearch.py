def binarySearch(arr, target):
    left = 0
    right = len(arr) - 1
    

    while left <= right:
        mid = (left + right)//2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            right = mid -1
        else:
            left = mid + 1
    return -1

list = [2,5,13,66,70,300,700,14000]

print(binarySearch(list, 300))