#imports django
from django.urls import path

#views import
from .views import Index,ProdutosAllApi,ProdutosView,Pesquisa_produto

#urls
urlpatterns = [
    path('',Index, name="index"),
    path('produtos/quantia/<int:quantia>',ProdutosAllApi.as_view(), name="produtos_all"),
    path('produtos/<str:nome>',ProdutosView.as_view(), name="produto"),
    path('pesquisa/<pesquisa>',Pesquisa_produto,name='pesquisa'),
    
]
