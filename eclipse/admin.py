from django.contrib import admin

#models import
from .models import Produtos

#models admin
class ProdutosAdmin(admin.ModelAdmin):
    model = Produtos
    list_display = ("nome", "preço")
    prepopulated_fields = {'slug': ['nome']}
    search_fields = ("nome",'preço')
    search_help_text = "presquise por nome ou preço"

# Register your models here.
admin.site.register(Produtos, ProdutosAdmin)