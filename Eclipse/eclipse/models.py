from django.db import models

# Create your models here.

class Categorias(models.TextChoices):
    GAMER = 'G','Gamer'
    UPGRADE = "U","Upgrade"
    ESCRITORIO = "E","Escritorio"
    

class Produtos(models.Model):
    Nome = models.CharField(max_length=50,unique=True)
    Preço = models.FloatField(null=False)
    Descrição = models.TextField(null=False)
    Imagem = models.ImageField(upload_to='media/',null=False)
    Categoria = models.CharField(max_length=3,choices=Categorias.choices,default=Categorias.ESCRITORIO)
    
    def __str__(self):
        return self.Nome
    
class Produto_Cor(models.Model):
    Produto = models.ForeignKey(Produtos,null=False,on_delete=models.CASCADE)
    Cor = models.CharField(max_length=50,)
    Cor_code = models.CharField(max_length=10,default='#ffffff')
    Preço = models.FloatField(null=False)
    Imagem = models.ImageField(upload_to='cores_produto/')
    
class Promoção(models.Model):
    Produto = models.ForeignKey(Produtos,on_delete=models.CASCADE)
    Desconto = models.FloatField(null=False,default=0)
    Criada = models.DateTimeField(auto_now_add=True)
    Acaba = models.DurationField()
    Estado = models.CharField(max_length=30,choices={
        "E": "Expirado",
        'V': "Valido",
    },default={'V','Valido'})
    
    def __str__(self):
        return f'{self.Produto} : {self.Desconto}'
    
    