def hello(name=''):
    if name=='':
        return 'Hello, World!'
    name=name.lower()
    name=name[0].upper()+name[1:]
    return 'Hello, ' + name +'!'
