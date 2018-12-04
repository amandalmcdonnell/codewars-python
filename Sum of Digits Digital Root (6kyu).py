def digital_root(n):
    # ...
    ans=0
    while len(str(n))>1:
        for i in range(len(str(n))):
            ans=ans+int(str(n)[i])
        n=ans
        ans=0
    print(n)
    return (n)def to_camel_case(text):
    #your code he
    c = '-'
    d ='_'
    t=0
    ans=''
    post=[]
    print(text)
    post=([pos for pos, char in enumerate(text) if char == c])+([pos for pos, char in enumerate(text) if char == d])
    post.sort()
    for i in post:
        #print(post)
        #print(text[i])
        if i+2<=len(text)-1:
            text=(text[:i+1]+text[i+1].upper()+text[i+2:])
            print(1)
        elif i+1<=len(text)-1:
            text=(text[:i+1]+text[i+1].upper())
            print(2)
        else:
            text=(text[:i])
            print(3)
    print(text)
    for j in post:
        text=text[:j-t]+text[j-t+1:]
        t=t+1
    print(text)
    print(post)
    return(text)
