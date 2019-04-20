# Shell sort algorithm 
# 20.04.2019

def shellsort(arr):
    sublistcount = len(arr) //2
    while sublistcount>0:
        for start_pos in range(sublistcount):
            gap_insertsort(arr,start_pos,sublistcount)
        print("After increments of size",sublistcount,"The list is ",arr)
        sublistcount = sublistcount //2

def gap_insertsort(arr,start_pos,gap):
    for i in range(start_pos+gap,len(arr),gap):
        currValue   = arr[i]
        position    = i
        while position>=gap and arr[position-gap]>currValue:
            arr[position]=arr[position-gap]
            position=position-gap
        arr[position]=currValue
arr = [14,46,43,27,57,41,45,21,70]
shellsort(arr)

