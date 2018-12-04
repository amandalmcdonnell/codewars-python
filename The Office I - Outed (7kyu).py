def outed(meet, boss):
    count=0
    for i in meet:
        if i==boss:
            count=count+meet[boss]*2
        else:
            count=count+meet[i]
    if (count/len(meet))<=5:
        return 'Get Out Now!'

    return 'Nice Work Champ!'
