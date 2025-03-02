#django imports
from django.shortcuts import render,redirect
from django.urls import reverse 
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect

#restframework imports
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

#jwt imports
from rest_framework_simplejwt.tokens import RefreshToken

#funçoes utilitaria
from .utils.jwt import pegar_user_jwt

#froms import
from .forms import LoginForm,CadastrarForm,EndereçoForms

#models import
from .models import Carriho,Produtos,Endereço

from json import dumps,loads

# Create your views here.
class UserEnter(View):
    def get(self, request):
        user = pegar_user_jwt(request)
        error = request.GET.get('error',False)
        if user == None:
            formulario_login = LoginForm()
            formulario_cadastro = CadastrarForm()
            context = {'form_login' : formulario_login,'form_cadastro' : formulario_cadastro,"error" : error}
            return render(request, "forms/user_enter.html",context=context)
        
        return redirect('perfil')
#falta o tratamento de erro
class UserLogin(APIView):
    def post(self, request):
        try:
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
                
            return redirect("/user/?error=senha invalido")
                    
                
        except User.DoesNotExist:
            return redirect(f"/user/?error=user invalido")
        
        
#falta o tratamento de erro
class UserRegister(APIView):
    def post( self, request ):
        Formulario = CadastrarForm(request.POST)
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
            cookie = request.COOKIES.get('carrinho',None)
            if cookie != None:
                itens = loads(cookie)
                produtos = []
                for item in itens:
                    produto = Produtos.objects.filter(Nome=item).first()
                    produtos.append(produto)
                context['carrinho_local'] = produtos
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
        respose = Response({},status=status.HTTP_200_OK)
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
        if user == None:
            carrinho_cookie = request.COOKIES.get("carrinho",dumps([]))
            carrinho_cookie = loads(carrinho_cookie)
            carrinho_cookie.append(produto.Nome)
            respose.set_cookie('carrinho',dumps(carrinho_cookie))

        return respose
    
class Endereços_Form_View(View):
    def get(self,request):
        context = {'form' : EndereçoForms()}
        return render(request,"forms/endereços.html",context=context)
    def post(self,request):
        form = EndereçoForms(request.POST)
        user = pegar_user_jwt(request)
        if form.is_valid():
            endereço = Endereço(User = user,Cep = form.cleaned_data["Cep"],Cidade = form.cleaned_data["Cidade"],Rua = form.cleaned_data['Rua'],Endereço = form.cleaned_data['Endereço'],Complemento = form.cleaned_data['Complemento'],Referencia = form.cleaned_data["Referencia"] ,Telefone = form.cleaned_data["Telefone"])           
            endereço.save()
            return redirect('endereço_view')
    
class Endereços_view(View):
    def get(self,request):
        user = pegar_user_jwt(request)
        endereços = Endereço.objects.filter(User = user).all()
        
        context = {"endereços":endereços}
        
        return render(request,'endereços.html',context=context)
    
    
class PedidosView(View):
    def get(self,request):
        context = {}
        return render(request,"pedidos.html",context=context)
    
class Logout(View):
    def get(self,request):
        response = redirect('index')
        response.delete_cookie('access')
        return response
    
class DadoUserView(View):
    def get(self,request):
        user = User.objects.get(username = pegar_user_jwt(request))
        context = {'user':user}
        return render(request,'dados.html',context=context)