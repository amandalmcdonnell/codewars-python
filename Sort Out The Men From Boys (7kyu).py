def men_from_boys(arr):
    new=[]
    new1=[]
    for i in arr:
        if i%2==0 and i not in new:
            new.append(i)
    new.sort()
    for i in arr:
        if i%2!=0 and i not in new1:
            new1.append(i)
    new1.sort(reverse=True)
    new=new+(new1)
    return new
