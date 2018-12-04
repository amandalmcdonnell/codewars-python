import math
def olympic_ring(string):
    li='ADOPQRabdegopq'
    count=0
    for x in string:
        if x in li:
            count=count+1
        elif x=='B':
            count=count+2
    count=math.floor(count/2)
    if count<2:
        return 'Not even a medal!'
    elif count==2:
        return 'Bronze!'
    elif count==3:
        return 'Silver!'
    else:
        return 'Gold!'
