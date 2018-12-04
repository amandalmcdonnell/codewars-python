import string
def cake(candles,debris):
    if (candles)==0:
        return 'That was close!'
    else:
        sum=0
        alp='abcdefghijklmnopqrstuvwxyz'
        for i in range(len(debris)):
            if i%2==0:
                sum=sum+(ord(debris[i]))
            if i%2!=0:
                sum=sum+((alp.find(debris[i]))+1)
        if (sum/candles)>0.7:
            return 'Fire!'
        return 'That was close!'
