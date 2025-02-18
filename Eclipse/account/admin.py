#django imports
from django.contrib import admin

#models import
from .models import Carriho,Endereço
from django.contrib.auth.models import User


#inlines
class CarrinhoInline(admin.TabularInline):
    model = Carriho
    extra = 1

class EndereçoInline(admin.TabularInline):
    model = Endereço
    extra = 0

#proxy
class ProxyUser(User):
    class Meta:
        proxy = True

#models admin
class CarrinhoAdmin(admin.ModelAdmin):
    list_display = ("User",'Produtos','Quantia')
    search_fields = ("User_username",'Produtos_Nome')

class EndereçoAdmin(admin.ModelAdmin):
    list_display= ("User","Cidade")
    
class UserAdmin(admin.ModelAdmin):
    inlines = [CarrinhoInline,EndereçoInline]
    list_display = ["username",'email']
    fields = ['username','email','groups']
    list_filter = ['groups']

# Register your models here.
admin.site.register(Carriho,CarrinhoAdmin)
admin.site.register(Endereço,EndereçoAdmin)
admin.site.register(ProxyUser,UserAdmin)