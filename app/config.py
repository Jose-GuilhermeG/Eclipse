FLASK_ENV = 'env'
SECRET_KEY = 'GW3LhQFe1LC/c94GMpOX5gPxi9ILGJLzDOPzk1DfMJKgYU5EEaP2rozZKfQhH0Ob'
TESTING = True
TEMPLATES_FOLDER = './templates'
STATIC_FOLDE = './static'

#db
from os import path

diretorio_base = path.abspath(path.dirname(__file__))
caminho = path.join(diretorio_base,'database.db')

SQLALCHEMY_DATABASE_URI = f"sqlite:///{caminho}"
SQLALCHEMY_TRACK_MODIFICATIONS = False

#jwt
JWT_SECRET_KEY = '1Ax7kysPJ5'
JWT_TOKEN_LOCATION = ['cookies']
JWT_ACCESS_COOKIE_NAME = 'Eclipse'