def format_duration(seconds):
    if seconds==0:
        return 'now'
    ar={"day": 0,"hour": 0, "minute":0,"second":0,"year": 0}
    order=["year","day","hour","minute","second"]
    str1=''
    while seconds>(365*24*60*60)-1:
        ar["year"]=ar["year"]+1
        seconds=seconds-(365*24*60*60)
    while seconds>(24*60*60)-1:
        ar["day"]=ar["day"]+1
        seconds=seconds-(24*60*60)
    while seconds>(60*60)-1:
        ar["hour"]=ar["hour"]+1
        seconds=seconds-(60*60)
    while seconds>59:
        ar["minute"]=ar["minute"]+1
        seconds=seconds-(60)
    ar["second"]=seconds
    ar1={"year":0,"day":(ar["day"]!=0),"hour":(ar["hour"]!=0),"minute":(ar["minute"]!=0),"second":(ar["second"]!=0)}
    for i in order:
        if ar[i]>0:
            str1=str1+(str(ar[i]) +' ' + i)
            if ar[i]>1:
                str1=str1+('s')
            del ar1[i]
            if sum(ar1.values())>1:
                str1=str1+(', ')
            elif sum(ar1.values())==1:
                str1=str1+(' and ')
    return(str1)
    
