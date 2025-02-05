#django imports
from django.contrib import admin

#models import
from .models import Carriho

#models admin
class CarrinhoAdmin(admin.ModelAdmin):
    list_display = ("User",'Produtos','Quantia')
    search_fields = ("User_username",'Produtos_Nome')

# Register your models here.
admin.site.register(Carriho,CarrinhoAdmin)