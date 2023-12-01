
def MergeSort(arr):
    n = len(arr)
    if len(arr) == 1:
        return  arr

    left = arr[0:n//2]
    right = arr[n//2:]
    left = MergeSort(left)
    right = MergeSort(right)

    return merge(left,right)

def merge(a,b):
    c = []
    while a != [] and b != []:
        if a[0] > b[0]:
            c.append(b[0])
            b.pop(0)
        else:
            c.append(a[0])
            a.pop(0)

    while a != []:
        c.append(a[0])
        a.pop(0)
    
    while b != []:
        c.append(b[0])
        b.pop(0)
    return c

list = [2,8,5,3,9,4,1,7]

print(MergeSort(list))
