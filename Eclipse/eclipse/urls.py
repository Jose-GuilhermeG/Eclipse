#imports django
from django.urls import path

#views import
from .views import Index,ProdutosAllApi

#urls
urlpatterns = [
    path('',Index.as_view(), name="index"),
    path('produtos/quantia/<int:quantia>',ProdutosAllApi.as_view(), name="produtos_all"),
    
]
