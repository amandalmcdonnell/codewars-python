def is_narcissistic(i):
    num=0
    for x in range(len(str(i))):
        num=num+int(str(i)[x])**len(str(i))
    return i==num
