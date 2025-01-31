from django.contrib import admin

#imports
from .models import Produtos

#models admin
class ProdutosAdmin(admin.ModelAdmin):
    class Meta:
        model = Produtos
        fields = ["id", "Nome",'Preço']


# Register your models here.
admin.site.register(Produtos, ProdutosAdmin)