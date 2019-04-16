#binary search algorithm 
#works only on sorted arrays. 


def binarysearch(a,length,key):
    low     = 0
    high    = length
    while low<=high:
        mid = int(low + (high - low)/2) 
        if a[mid] ==  key:
            return a[mid]
        elif a[mid]>key:
            high = mid-1
        else:
            low = mid+1
    return -1
    
array   = [11,22,33,44,55,66,77]
length  = len(array) -1
key     = 45
out     = binarysearch(array,length,key)
if out == key:
    print('Element is found')
else:
    print('Not found')