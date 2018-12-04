#yes this was a dumb way to do it
def count_positives_sum_negatives(arr):
    countp=0
    countn=0
    print(arr)
    if arr==[]:
        return arr
    for i in range(len(arr)):
        if(int(arr[i])==abs(int(arr[i]))) and arr[i]!=0:
            countp=countp+1
            print(arr[i])
        elif arr[i]*(-1)>0:
            countn=countn+int(arr[i])
            print(arr[i])
    return [countp, countn]
    
