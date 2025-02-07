#restframework imports
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

#models import
from .models import Produtos,Promoção,Categorias

class PromoçãoSerializers(ModelSerializer):
    estado = serializers.CharField(source = 'get_Estado_display', read_only = True)
    class Meta:
        model = Promoção
        fields = ["Desconto", "estado",'Acaba']

class ProdutosSerializers(ModelSerializer):
    promoções = serializers.SerializerMethodField()
    categoria = serializers.CharField(source='get_Categoria_display', read_only=True)
    class Meta:
        model = Produtos
        fields = ['id','Nome','Preço','Descrição','Imagem','categoria','promoções']
        
    def get_promoções(self,obj):
        promoções = Promoção.objects.filter(Produto = obj)
        return PromoçãoSerializers(promoções,many = True).data