#Selection sort 

def selectionSort(arr,n):
    for i in range(n-1):
        small   = i
        for j in range(i+1,n):
            if arr[j]<arr[small]:
                small = j
        if i!=small:
            arr[i], arr[small] = arr[small], arr[i] 
    return arr


a   =   [45,38,59,12,66,23]
out =   selectionSort(a,len(a))
print('length of the array is ',len(a))
print('sorted array ',out)