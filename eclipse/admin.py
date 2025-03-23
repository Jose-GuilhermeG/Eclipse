from django.contrib import admin

#models import
from .models import Produtos,Categorias,Categorias_Produtos,Variantes

class ProdutosCategoriasInline(admin.TabularInline):
    model = Categorias_Produtos
    extra = 1

#models admin
class ProdutosAdmin(admin.ModelAdmin):
    model = Produtos
    inlines = [ProdutosCategoriasInline]
    list_display = ("nome", "preço")
    prepopulated_fields = {'slug': ['nome']}
    search_fields = ("nome",'preço')
    search_help_text = "presquise por nome ou preço"
    
class CategoriasAdmin(admin.ModelAdmin):
    model = Categorias
    list_display = ("nome",)
    prepopulated_fields = {"slug":['nome']}
    search_fields = ("nome","slug")
    search_help_text = "pesquisar por nome ou atalho"
    
class VariantesAdmin(admin.ModelAdmin):
    model = Variantes
    list_display = ("nome",'produto')
    

# Register your models here.
admin.site.register(Produtos, ProdutosAdmin)
admin.site.register(Categorias,CategoriasAdmin)
admin.site.register(Categorias_Produtos)
admin.site.register(Variantes,VariantesAdmin)