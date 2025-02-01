from django.db import models

# Create your models here.
class Produtos(models.Model):
    Nome = models.CharField(max_length=50,unique=True)
    Preço = models.FloatField(null=False)
    Descrição = models.TextField(null=False)
    Imagem = models.ImageField(upload_to='media/',null=False)