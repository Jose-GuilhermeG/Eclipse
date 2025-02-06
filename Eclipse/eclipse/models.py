from django.db import models

# Create your models here.
class Produtos(models.Model):
    Nome = models.CharField(max_length=50,unique=True)
    Preço = models.FloatField(null=False)
    Descrição = models.TextField(null=False)
    Imagem = models.ImageField(upload_to='media/',null=False)
    
    def __str__(self):
        return self.Nome
    
class Produto_Cor(models.Model):
    Produto = models.ForeignKey(Produtos,null=False,on_delete=models.CASCADE)
    Cor = models.CharField(max_length=50,)
    Cor_code = models.CharField(max_length=10,default='#ffffff')
    Preço = models.FloatField(null=False)
    Imagem = models.ImageField(upload_to='cores_produto/')