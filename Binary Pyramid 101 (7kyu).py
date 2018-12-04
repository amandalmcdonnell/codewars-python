def binary_pyramid(m,n):
    sum=0
    for k in range(m,n+1):
        sum=sum+(int(str(bin(k))[2:]))
    return str(bin(sum))[2:]
