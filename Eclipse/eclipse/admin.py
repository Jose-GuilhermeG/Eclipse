from django.contrib import admin

#imports
from .models import Produtos

#models admin
class ProdutosAdmin(admin.ModelAdmin):
    list_display = ['id','Nome','Preço']


# Register your models here.
admin.site.register(Produtos, ProdutosAdmin)