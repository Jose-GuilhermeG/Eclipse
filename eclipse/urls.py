#django imports
from django.urls import re_path

#views imports
from .views import Index,ProdutoView,ProdutosAllView,CategoriasProdutosView,PesquisarProdutosView

urlpatterns = [
    re_path(r'^$',Index.as_view(),name="index"),
    re_path(r'^produtos/(?P<slug>[\w-]+)/$',ProdutoView.as_view(),name="produto"),
    re_path(r"^produtos/all$",ProdutosAllView.as_view(),name="produtos_all"),
    re_path(r'^produtos/categorias/(?P<categoria>[\w_-]+)/$',CategoriasProdutosView.as_view(),name='categorias'),
    re_path(r'^pesquisa/(?P<pesquisa>[\w_-]+)/$',PesquisarProdutosView.as_view(),name='pesquisa'),
]
