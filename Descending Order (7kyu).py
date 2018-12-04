def Descending_Order(num):
    k=[]
    dummy=str(num)
    ans=''
    for i in range(len(dummy)):
        k.append(dummy[i])

    k.sort(reverse=True)
    for j in range(len(dummy)):
        ans=ans+str(k[j])

    return(int(ans))
