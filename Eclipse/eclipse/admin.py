from django.contrib import admin

#imports
from .models import Produtos,Produto_Cor

#models admin
class ProdutosAdmin(admin.ModelAdmin):
    list_display = ['id','Nome','Preço']
    
class ProdutoCorAdmin(admin.ModelAdmin):
    list_display = ['Produto','Cor']


# Register your models here.
admin.site.register(Produtos, ProdutosAdmin)
admin.site.register(Produto_Cor,ProdutoCorAdmin)