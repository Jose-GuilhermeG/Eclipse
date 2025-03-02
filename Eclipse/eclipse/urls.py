#imports django
from django.urls import path

#views import
from .views import Index,ProdutosAllApi,ProdutosView,Pesquisa_produto,ProdutosCategoriasView,Pesquisa_produto_view,FilterProdutos,Sobre

#urls
urlpatterns = [
    path('',Index, name="index"),
    path('sobre',Sobre.as_view(), name="sobre"),
    path('produtos/',ProdutosAllApi.as_view(), name="produtos_all"),
    path('produtos/filter',FilterProdutos.as_view(), name="filter"),
    path('produtos/<str:nome>',ProdutosView.as_view(), name="produto"),
    path('pesquisa/',Pesquisa_produto,name='pesquisa'),
    path('pesquisa/<pesquisa>',Pesquisa_produto_view.as_view(),name='pesquisa_view'),
    path('categorias/<categoria>',ProdutosCategoriasView.as_view(),name='Categoria_view'),
]
