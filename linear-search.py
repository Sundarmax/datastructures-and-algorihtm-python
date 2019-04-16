#Linear search in normal array
#Linear search in sorted array

def search(a,key):
    for i in range(len(a)-1):
        if a[i] == key:
            return a[i]
    return -1

def sorted(b,key):
    for j in range(len(b)-1):
        if b[j] == key:
            return b[i]
        elif b[j]> key:
            break
    print(j)
    return -1

a       = [3,5,4,3,2,1]
b       = [22,33,44,55,66,77]
key     = 7
keyb    = 45 
out = search(a,key)
if out == key:
    print('element is found')
else:
    print('element is not found')
bout = sorted(b,keyb)
if bout == key:
    print('element is found')
else:
    print('element is not found')
