from random import choice

tokens = []

def create_token(user):
    token = ''
    for letra_numero in range(choice([10,15,20])):
        lista = '0123456789abcdefghijkmnopqrstuvwxyz!@#$%&*~^'
        token += choice(lista)

    apend = {'user' : user, 'token' : token}

    tokens.append(apend)
    return token

def check_token(user, token):
    for elements in tokens:
        if elements['user'] == user and elements['token'] == token:
            return True
        
    return False
        
            