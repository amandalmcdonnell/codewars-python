def get_middle(s):
    #your code here
    if ((len(s)%2))==0:
        return(s[(-1+len(s)/2)]+s[(len(s)/2)])

    if ((len(s)%2))==1:
        return(s[(len(s)/2)])
