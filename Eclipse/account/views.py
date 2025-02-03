#django imports
from django.shortcuts import render
from django.views import View

#froms import
from .forms import LoginForm,CadastrarForm

# Create your views here.
class UserEnter(View):
    def get(self, request):
        formulario_login = LoginForm()
        formulario_cadastro = CadastrarForm()
        context = {'form_login' : formulario_login,'form_cadastro' : formulario_cadastro}
        return render(request, "forms/user_enter.html",context=context)


def Carrinho(request):
    user = request.user
    context = {'carrinho' : request.session.get('carrinho',None)}
    response = render(request, "carrinho.html",context=context)
    return response