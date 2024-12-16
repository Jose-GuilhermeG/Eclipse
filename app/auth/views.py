from flask import render_template,redirect,request,jsonify
from .bp import auth

@auth('/',methods = ['GET'])
def index_user():
    return render_template("user.html",)

@auth("/login",methods = ['GET','POST'])
def login():
    if request.method == "POST":
        return 'em trabalho ainda'
    
    return render_template('forms/login_register.html')