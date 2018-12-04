import math
def is_square(n):
    if n>-1:
        if (math.sqrt(n)-(math.floor(math.sqrt(n))))==0:
            return True
    return False
