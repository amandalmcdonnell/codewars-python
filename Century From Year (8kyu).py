def century(year):
    if year<100:
        return 1
    if int(str(year)[(-2):])==0:
        return int(str(year)[:(-2)])
    return int(str(year)[:(-2)])+1
