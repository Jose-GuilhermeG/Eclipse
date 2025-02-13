#restframework imports
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

#models import
from .models import Produtos,Promoção,Categorias,Produto_Cor

class PromoçãoSerializers(ModelSerializer):
    estado = serializers.CharField(source = 'get_Estado_display', read_only = True)
    class Meta:
        model = Promoção
        fields = ["Desconto", "estado",'Acaba']
        
class ProdutoCorSerializers(ModelSerializer):
    class Meta:
        model = Produto_Cor
        fields = ["Cor", "Cor_code","Preço","Imagem"]

class ProdutosSerializers(ModelSerializer):
    promoções = serializers.SerializerMethodField()
    cores = serializers.SerializerMethodField()
    categoria = serializers.CharField(source='get_Categoria_display', read_only=True)
    class Meta:
        model = Produtos
        fields = ['id','Nome','Preço','Descrição','Imagem','categoria','promoções','cores']
        
    def get_promoções(self,obj):
        promoções = Promoção.objects.filter(Produto = obj)
        return PromoçãoSerializers(promoções,many = True).data
    def get_cores(self,obj):
        cores = Produto_Cor.objects.filter(Produto = obj)
        return ProdutoCorSerializers(cores,many = True).data