def find_uniq(arr):
    c=0
    d=0
    c=arr.count((max(arr)))
    if c==1:
        return max(arr)
    else:
        return min(arr)
