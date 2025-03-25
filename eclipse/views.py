#django imports
from django.views.generic import TemplateView,DetailView,ListView
from django.core.paginator import Paginator


#models
from .models import Produtos,Variantes

#filtros
from .filters import ProdutosFilter
from django_filters.views import FilterView

#mixin
from .mixin import MultiItensView

# Create your views here.
class Index(MultiItensView,TemplateView):
    template_name = "index.html"
    extra_context = {'produto_mes' : Produtos.objects.get(id=2)}
    pages_name = 'page'
    model = Produtos
    paginate_by = 6
    context_object_name = 'produtos'
    
    
#views produtos

class ProdutoView(DetailView):
    queryset = Produtos.objects.all()
    template_name = "produto.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    context_object_name = "produto"
    
class ProdutosAllView(FilterView):
    #list
    template_name = 'generic_list.html'
    paginate_by = 10
    context_object_name = "produtos"
    extra_context = {'vazio_menssagem' : 'parece que não temos nenhum produto'}
    #filter
    model = Produtos
    filterset_class = ProdutosFilter
    
class CategoriasProdutosView(ListView):
    template_name="generic_list.html"
    context_object_name="produtos"
    paginate_by=10
    extra_context = {'vazio_menssagem' : 'nenhum produto para essa categoria'}
    
    def get_queryset(self):
        categoria = self.kwargs.get("categoria", "")
        return Produtos.objects.pegar_produtos_por_categoria(categoria)

class PesquisarProdutosView(ListView):
    template_name="generic_list.html"
    context_object_name ='produtos'
    paginate_by=10
    extra_context = {"vazio_menssagem" : "Não ha resultados para essa pesquisa"}
    
    def get_queryset(self):
        pesquisa = self.kwargs.get("pesquisa")
        return Produtos.objects.pesquisa(pesquisa)