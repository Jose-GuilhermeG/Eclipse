from django.db import models

# Create your models here.
class Produtos(models.Model):
    Nome = models.CharField(max_length=50,unique=True)
    Preço = models.FloatField(null=False)
    Descrição = models.TextField(null=False)
    Imagem = models.ImageField(upload_to='media/',null=False)
    
class Produto_Cor(models.Model):
    Produto = models.ForeignKey(Produtos,null=False,on_delete=models.CASCADE)
    Cor = models.CharField(max_length=50,)
    Preço = models.FloatField(null=False)
    Imagem = models.ImageField(upload_to='cores_produto/')