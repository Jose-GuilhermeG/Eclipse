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