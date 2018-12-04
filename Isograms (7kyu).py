def is_isogram(string):
    #your code here
    string=string.lower()
    goal=(len(string))
    j=0
    count=0
    for c in string:
        string=string[1:]
        if string.find(c)!=-1:
            count=count+1
    if count>0:
        return(False)
    else:
        return(True)
