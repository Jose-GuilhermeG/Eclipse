#django imports
from django.urls import path

#views imports
from .views import Carrinho,UserEnter

#urls

urlpatterns = [
    path("carrinho/", Carrinho,name='carrinho'),
    path("", UserEnter.as_view(),name='user'),
]
