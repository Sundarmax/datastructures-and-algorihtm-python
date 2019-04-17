# Insertition sort algorithm 

def insertition_sort(arr,n):
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1] = key

    return arr
arr     =[85,12,59,45,72,51]
result  =insertition_sort(arr,len(arr))
print(result)