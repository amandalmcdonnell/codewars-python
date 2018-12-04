def series_sum(n):
    s=1
    c=4
    if n==0:
        return '0.00'
    if n==1:
        return '1.00'
    else:
        for x in range(n-1):
            s=s+1/c
            c=c+3
    return ('%.2f' % s)
