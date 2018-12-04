import datetime
def date_nb_days(a0, a, p):
    dayf=0
    while a0<a:
        a0=a0+(a0*(p/36000))
        dayf=dayf+1
    x=datetime.datetime(2016, 1, 1)+datetime.timedelta(days=dayf)
    return (str(x)[:10])
