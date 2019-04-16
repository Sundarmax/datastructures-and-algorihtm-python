def bubblesort(arr,n):
    for i in range(n):
        for j in range(0,n-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr


arr = [45,23,59,66,38,12]
out = bubblesort(arr,len(arr)-1)
print(out)