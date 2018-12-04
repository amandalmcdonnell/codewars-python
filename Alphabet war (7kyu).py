def alphabet_war(fight):
    r=l=0
    left={"w": 4, "p": 3,"b": 2,"s": 1}
    right={"m": 4, "q": 3,"d": 2,"z": 1}
    for i in fight:
        if i in right:
            r=r+right[i]
        if i in left:
            l=l+left[i]
    if l>r:
        return 'Left side wins!'
    if l<r:
        return 'Right side wins!'
    return 'Let\'s fight again!'
