def SelectionSort(arr):
   
    for i in range(len(arr)):
        smallest = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest]:
                smallest = j
        if(smallest != i):
            swap(arr, smallest, i)
    return arr

def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


list = [2,8,5,3,9,4,1]

print(SelectionSort(list))
        
               

        
            
       