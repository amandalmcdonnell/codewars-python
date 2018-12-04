import math
def cut_fruits(fruits):
    out=[]
    for x in fruits:
        if x in (FRUIT_NAMES):
            out.append(x[:math.ceil((len(x))/2)])
            out.append(x[math.ceil((len(x))/2):])
        else:
            out.append(x)
    return out
