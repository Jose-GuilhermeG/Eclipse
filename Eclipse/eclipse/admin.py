from django.contrib import admin

#imports
from .models import Produtos,Produto_Cor,Promoção

#models admin
class ProdutosAdmin(admin.ModelAdmin):
    list_display = ['id','Nome','Preço']
    search_fields = ['Nome']
    list_filter = ['Nome','Preço']
    
class ProdutoCorAdmin(admin.ModelAdmin):
    list_display = ['Produto','Cor']
    search_fields = ['Produto','Cor']
    
class PromoçãoAdmin(admin.ModelAdmin):
    list_display = ["Produto","Desconto",'Acaba','Estado']
    search_fields = ['Produto','Estado']


# Register your models here.
admin.site.register(Produtos, ProdutosAdmin)
admin.site.register(Produto_Cor,ProdutoCorAdmin)
admin.site.register(Promoção,PromoçãoAdmin)

#personalização
admin.site.site_title = 'Eclipse admin'
admin.site.site_header = 'Administração Eclipse'
admin.site.index_title = 'Eclipse'