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
    from .main.bp import main as main_bp
    from .auth.bp import auth as auth_bp
    from .produto.bp import produto as produto_bp

    app.register_blueprint(main_bp,url_prefix = '/')
    app.register_blueprint(auth_bp,url_prefix = "/user")
    app.register_blueprint(produto_bp,url_prefix = '/produto')

    @app.route('/test',methods = ['GET'])
    def teste_rota():
        return '<h1> essa é uma rota de teste</h1>'
    
    try:
        with app.app_context():
            db.create_all()

    except Exception as e:
        print(e)
    
    return app