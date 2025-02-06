from django.contrib import admin

#imports
from .models import Produtos,Produto_Cor,Promoção

#models admin
class ProdutosAdmin(admin.ModelAdmin):
    list_display = ['id','Nome','Preço']
    
class ProdutoCorAdmin(admin.ModelAdmin):
    list_display = ['Produto','Cor']
    
class PromoçãoAdmin(admin.ModelAdmin):
    list_display = ["Produto","Desconto",'Estado']


# Register your models here.
admin.site.register(Produtos, ProdutosAdmin)
admin.site.register(Produto_Cor,ProdutoCorAdmin)
admin.site.register(Promoção,PromoçãoAdmin)