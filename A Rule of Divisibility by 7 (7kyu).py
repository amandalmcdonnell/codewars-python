def seven(m):
    count=0
    while len(str(m))>2:
        m=int(str(m)[:-1])-2*int(str(m)[-1])
        count+=1
    return (m,count)
