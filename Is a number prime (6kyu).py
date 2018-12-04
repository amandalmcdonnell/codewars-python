import math
def is_prime(num):
  if num==2:
      return(True)
  if num<=1 or (num%2==0 and num!=2):
      return(False)
  for i in range(int(math.floor(num/2))):
      if num%(i+2)==0:
          return(False)
  return(True)
  
