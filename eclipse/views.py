#django imports
from django.views.generic import TemplateView,DetailView,ListView
from django.core.paginator import Paginator


#models
from .models import Produtos

# Create your views here.
class Index(TemplateView):
    template_name = "index.html"
    extra_context = {'produto_mes' : Produtos.objects.get(id=2)}

#views produtos

class ProdutoView(DetailView):
    queryset = Produtos.objects.all()
    template_name = "produto.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    context_object_name = "produto"
    
class ProdutosAllView(ListView):
    queryset = Produtos.objects.all()
    template_name = 'produtos_all.html'
    paginate_by = 10
    context_object_name = "produtos"