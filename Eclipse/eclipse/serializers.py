#restframework imports
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

#models import
from .models import Produtos,Promoção,Categorias

class PromoçãoSerializers(ModelSerializer):
    class Meta:
        model = Promoção
        fields = ("Desconto", "Estado")

class ProdutosSerializers(ModelSerializer):
    promoção = PromoçãoSerializers(many = True,read_only=True)
    categoria = serializers.CharField(source='get_Categoria_display', read_only=True)
    class Meta:
        model = Produtos
        fields = ['id','Nome','Preço','Descrição','Imagem','categoria','promoção']