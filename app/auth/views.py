from flask import render_template,redirect,request,jsonify,make_response
from flask_jwt_extended import jwt_required,get_current_user,create_access_token
from .bp import auth
from ..models import user
from ..db import db

@auth.route('/',methods = ['GET'])
@jwt_required(optional=True)
def index_user():
    print(get_current_user())
    return render_template("user.html",)

@auth.route("/login",methods = ['POST'])
def login():
    if request.content_type == 'application/json':
        Senha_user = request.get_json()["senha"]
        Email_user = request.get_json()["email"]
        if Email_user and Senha_user:
            existente = db.session.query(user).filter_by(email_user = Email_user).first()

            if existente:
                if existente.senha_check(Senha_user):
                    token = create_access_token(identity=existente)

                    reposta = make_response(jsonify({'logado':True}))

                    reposta.set_cookie('Eclipse',token)
                    return reposta
                reposta = make_response(jsonify({'err':'senha errada'}))
                return reposta

            reposta = make_response(jsonify({'err':'usuario não existe'}))
            return reposta
        reposta = make_response(jsonify({'err':'dados invalidos'}))
        return reposta   

    reposta = make_response(jsonify({'err':'tipo não suportado'}))
    return reposta
    
@auth.route('/register',methods = ['POST'])
def register():
    if request.content_type == "application/json":
        Nome_user = request.get_json()['nome']
        Senha_user = request.get_json()["senha"]
        Email_user = request.get_json()["email"]
        existente = db.session.query(user).filter_by(email_user = Email_user).first()
        if existente == None:
            if Nome_user and Senha_user and Email_user  :
                usuario = user(Nome_user, Senha_user,Email_user)
                try:
                    db.session.add(usuario)
                    db.session.commit()
                    reposta = make_response(jsonify({'register' : True}))

                    token = create_access_token(identity=usuario)
                    reposta.set_cookie('Eclipse',token)

                    return reposta
                except Exception as e:
                    print(e)
                    reposta = make_response(jsonify({'err':'interno'}))
                    return reposta
            reposta = make_response(jsonify({'err' : 'dados nulos'}))
            return  reposta     
        reposta = make_response(jsonify({"err": 'usuaio existente'}))

        return reposta
        

    reposta = make_response(jsonify({'err':'tipo não suportado'}))
    return reposta