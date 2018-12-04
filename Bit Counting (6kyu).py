def countBits(n):
    bitstring = ""
    n=int(n)
    bit=0
    ans=0
    while n>0:
        bit=int(n%2)
        quotient=int(n/2)
        bitstring=str(bit)+bitstring
        n=quotient
    for i in range(len(bitstring)):
        ans=ans+int(bitstring[i])
    return(ans)
