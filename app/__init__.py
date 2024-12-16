from flask import Flask, render_template
from flask_bcrypt import Bcrypt
from .db import db
from .jwt import jwt

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    #bcrypt
    bcrypt = Bcrypt(app)

    #database
    db.init_app(app)

    #jwt
    jwt.init_app(app)


    #bp and imports

    @app.route('/test',methods = ['GET'])
    def teste_rota():
        return '<h1> essa é uma rota de teste</h1>'
    
    return app