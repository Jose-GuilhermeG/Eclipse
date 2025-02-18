#django imports
from django.urls import path

#views imports
from .views import Carrinho_view,UserEnter,UserLogin,Perfil,UserRegister,Carrinho

#utils imports
from .utils.jwt import jwt_login_required

#urls

urlpatterns = [
    path("carrinho/", Carrinho_view,name='carrinho'),
    path("", UserEnter.as_view(),name='user'),
    path("login/", UserLogin.as_view(),name='user_login'),
    path("register/", UserRegister.as_view(),name='user_cadastro'),
    path("perfil/", jwt_login_required(Perfil.as_view()),name='perfil'),
    path('carrinho/add',Carrinho.as_view(),name="carrinho_add"),
]
