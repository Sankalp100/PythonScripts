# Search the value 'value' in the dataset 'l'.
# If succesful, returns the index in wich l[index]==value.
# Else returns -1.

def binary_search(l, value):
    low = 0
    high = len(l)-1
    while low <= high: 
        mid = (low+high)//2
        if l[mid] > value: high = mid-1
        elif l[mid] < value: low = mid+1
        else: return mid
    return -1
