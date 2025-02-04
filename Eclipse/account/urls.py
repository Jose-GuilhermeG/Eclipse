#django imports
from django.urls import path

#views imports
from .views import Carrinho,UserEnter,UserLogin,Perfil,UserRegister

#urls

urlpatterns = [
    path("carrinho/", Carrinho,name='carrinho'),
    path("", UserEnter.as_view(),name='user'),
    path("login/", UserLogin.as_view(),name='user_login'),
    path("register/", UserRegister.as_view(),name='user_cadastro'),
    path("perfil/", Perfil.as_view(),name='perfil'),
]
