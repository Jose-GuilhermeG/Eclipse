#django imports
from django.urls import re_path

#views imports
from .views import Index,ProdutoView,ProdutosAllView

urlpatterns = [
    re_path(r'^$',Index.as_view(),name="index"),
    re_path(r'^produtos/(?P<slug>[\w-]+)/$',ProdutoView.as_view(),name="produto"),
    re_path(r"^produtos/all$",ProdutosAllView.as_view(),name="produtos_all"),
]
