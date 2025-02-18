#django imports
from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

#restframework imports
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

#jwt imports
from rest_framework_simplejwt.tokens import RefreshToken

#funçoes utilitaria
from .utils.jwt import pegar_user_jwt

#froms import
from .forms import LoginForm,CadastrarForm

#models import
from .models import Carriho,Produtos

# Create your views here.
class UserEnter(View):
    def get(self, request):
        user = pegar_user_jwt(request)
        if user == None:
            formulario_login = LoginForm()
            formulario_cadastro = CadastrarForm()
            context = {'form_login' : formulario_login,'form_cadastro' : formulario_cadastro}
            return render(request, "forms/user_enter.html",context=context)
        
        return redirect('perfil')
#falta o tratamento de erro
class UserLogin(APIView):
    def post(self, request):
        Formulario = LoginForm(request.POST)
        if Formulario.is_valid():
            Email = Formulario.cleaned_data["Email"]
            Senha = Formulario.cleaned_data["Senha"]
            
            username = User.objects.get(email=Email)
            user = authenticate(username = username ,password = Senha)
            
            if user is not None:
                token = RefreshToken.for_user(user)
                response = redirect('perfil')
                response.set_cookie('access',str(token.access_token))
                
                return response
                
            

        return redirect('user')
#falta o tratamento de erro
class UserRegister(APIView):
    def post( self, request ):
        Formulario = CadastrarForm(request.POST)
        print(Formulario)
        if Formulario.is_valid():
            Nome = Formulario.cleaned_data["Nome"]
            Email = Formulario.cleaned_data['Email']
            Senha = Formulario.cleaned_data['Senha']
            
            user_existe = User.objects.filter(email=Email).first()
            
            if not user_existe:
                user = User(username = Nome,email = Email)
                user.set_password(Senha)
                user.save()
                token = RefreshToken.for_user(user)
                response = redirect("perfil")
                response.set_cookie('access',str(token.access_token))
                return response
            return redirect("user")
        
        return redirect("user")

def Carrinho_view(request):
    if request.method == "GET":
        user = pegar_user_jwt(request)
        context = {'user' : user}
        if user == None:
            context['carrinho'] = request.session.get('carrinho',None)
        else:
            carrinho = Carriho.objects.filter(User = user).all()
            context['carrinho'] = carrinho
            total = 0
            for item in carrinho:
                total += item.Produtos.Preço * item.Quantia
            context["Valor_total"] = total
                
        response = render(request, "carrinho.html",context=context)
        return response

class Perfil(View):
    def get(self,request):
        return render(request, "perfil.html",)
    
#falta o tratamento de erro
class Carrinho(APIView):
    def get(self, request):
        return redirect('carrinho')
    def post(self,request):
        user = pegar_user_jwt(request)
        quantia = request.data.get('quantia')
        produto = request.data.get('produto')
        produto = Produtos.objects.filter(Nome__icontains = produto).first()
        if user != None:
            ja_tem = Carriho.objects.filter(User = user,Produtos = produto).first()
            if ja_tem:
                produto_carrinho = Carriho.objects.get(id = ja_tem.id)
                print(produto_carrinho.Quantia)
                produto_carrinho.Quantia = produto_carrinho.Quantia + 1
                produto_carrinho.save()
            else:  
                carrinho_novo = Carriho(User = user,Produtos = produto,Quantia =quantia)
                carrinho_novo.save()
        return Response({},status=status.HTTP_200_OK)