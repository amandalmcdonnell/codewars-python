def find_outlier(integers):
    index=[]
    for i in range(len(integers)):
        index.append((integers[i])%2)
    if (sum(index))==1:
        return(integers[(index.index(1))])
    return(integers[(index.index(0))])
