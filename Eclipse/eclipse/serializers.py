#restframework imports
from rest_framework.serializers import ModelSerializer

#models import
from .models import Produtos

class ProdutosSerializers(ModelSerializer):
    class Meta:
        model = Produtos
        fields = ['id','Nome','Preço','Descrição','Imagem']     