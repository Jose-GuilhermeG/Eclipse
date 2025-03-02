#django imports
from django.urls import path

#views imports
from .views import Carrinho_view,UserEnter,UserLogin,Perfil,UserRegister,Carrinho,Endereços_view,Endereços_Form_View,PedidosView,Logout,DadoUserView

#utils imports
from .utils.jwt import jwt_login_required

#urls

urlpatterns = [
    path("", UserEnter.as_view(),name='user'),
    path("carrinho/", Carrinho_view,name='carrinho'),
    path("login/", UserLogin.as_view(),name='user_login'),
    path("register/", UserRegister.as_view(),name='user_cadastro'),
    path("perfil/", jwt_login_required(Perfil.as_view()),name='perfil'),
    path('perfil/endereços',jwt_login_required(Endereços_view.as_view()),name='endereço_view'),
    path('perfil/endereços/form',jwt_login_required(Endereços_Form_View.as_view()),name='endereço_form'),
    path('carrinho/add',Carrinho.as_view(),name="carrinho_add"),
    path('perfil/pedidos',jwt_login_required(PedidosView.as_view()),name="pedidos"),
    path('logout/',jwt_login_required(Logout.as_view()),name="logout"),
    path('perfil/dados',jwt_login_required(DadoUserView.as_view()),name="dados"),
]
