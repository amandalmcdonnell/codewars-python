def pig_it(text):
    t=''
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for i in text.split():
        if i not in punctuations:
            t=t+(i[1:]+i[0]+'ay'+' ')
        else:
            t=t+i+' '
    return(t[:len(t)-1])
