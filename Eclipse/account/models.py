#django import
from django.db import models
from django.contrib.auth.models import User

from eclipse.models import Produtos

# Create your models here.
class Carriho(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    Produtos = models.ForeignKey(Produtos,on_delete=models.CASCADE)
    Quantia = models.IntegerField(default=1)
    
    def __str__(self):
        return f'{self.User},{self.Produtos}'
    
class Endereço(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    Cep = models.IntegerField(null=False)
    Cidade = models.CharField(max_length=60,null=False)
    Rua = models.CharField(max_length=60,null=False)
    Endereço = models.IntegerField(null=False)
    Complemento = models.CharField(max_length=100,null=False)
    Referencia = models.TextField()
    Telefone =  models.IntegerField()

    def __str__(self) -> str:
        return f"{self.User} - {self.Cidade}"