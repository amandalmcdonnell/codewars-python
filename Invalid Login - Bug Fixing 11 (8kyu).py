def validate(username, password):

    if username.count('||')!=0 or username.count('//')!=0:
        return 'Wrong username or password!'
    database = Database()
    return (database.login(username, password))
