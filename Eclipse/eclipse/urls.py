#imports django
from django.urls import path

#views import
from .views import Index,ProdutosAllApi,ProdutosView,Pesquisa_produto,ProdutosCategoriasView,ProdutoExpecificoApi

#urls
urlpatterns = [
    path('',Index, name="index"),
    path('produtos/quantia/<int:quantia>',ProdutosAllApi.as_view(), name="produtos_all"),
    path('produtos/detalhes/<str:nome>',ProdutoExpecificoApi.as_view(), name="produto_expecifico"),
    path('produtos/<str:nome>',ProdutosView.as_view(), name="produto"),
    path('pesquisa/<pesquisa>',Pesquisa_produto,name='pesquisa'),
    path('categorias/<categoria>',ProdutosCategoriasView.as_view(),name='Categoria_view'),
]
