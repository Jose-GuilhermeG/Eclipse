#django filters
import django_filters

#models import
from .models import Produtos

#models filter

class ProdutosFilter(django_filters.FilterSet):
    preço_min = django_filters.NumberFilter(field_name="preço",lookup_expr="gte")
    preço_max = django_filters.NumberFilter(field_name="preço",lookup_expr="lte")
    
    class Meta:
        model = Produtos
        fields = {
            'preço' : ['gte','lte'],
            "categorias" : ["exact"],
        }