def find_nb(m):
    i=1
    while m>0:
            m=m-(i)**3
            i=i+1
    if m==0:
        return(i-1)
    else:
        return(-1)
