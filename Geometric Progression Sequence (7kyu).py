def geometric_sequence_elements(a, r, n):
    st=str(a)
    for i in range(n-1):
        a=a*r
        st=st+', '+str(a)
    return st
        
