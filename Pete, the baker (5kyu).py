def cakes(recipe, available):
    mini=[]
    for i in recipe:
        if i in available:
            mini.append(available[i]/recipe[i])
        else:
            return 0
    return(min(mini))
