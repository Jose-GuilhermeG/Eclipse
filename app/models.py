from .db import db
from flask_bcrypt import generate_password_hash,check_password_hash
from .jwt import jwt

@jwt.user_identity_loader
def user_identity_loader(user):
    return str(user.id)

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header,jwt_data):
    identify = jwt_data['sub']
    return user.query.filter_by(id = identify).first()



class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_user = db.Column(db.String(30), nullable=False)
    senha_user = db.Column(db.Text,nullable = False)
    email_user = db.Column(db.Text(),nullable=False,unique = True)

    def __init__(self,nome,senha,email):
        self.nome_user = nome
        self.senha_user = generate_password_hash(senha)
        self.email_user = email

    def senha_check(self,senha):
        return check_password_hash(self.senha_user,senha)
    
    def __repr__(self):
        return f'id:{self.id} User : {self.nome_user}'
    
class produto(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nome_produto = db.Column(db.String(50),nullable=False)
    preço = db.Column(db.Float(),nullable=False)
    imagen = db.Column(db.LargeBinary(),nullable=False)
    descrição = db.Column(db.Text(),nullable=True)

    def __init__(self,nome,preço,imagem,descrição):
        self.nome_produto = nome
        self.preço = preço
        self.imagen = imagem
        self.descrição = descrição

    def __repr__(self):
        return f'id_produto : {self.id},Nome : {self.nome_produto}'