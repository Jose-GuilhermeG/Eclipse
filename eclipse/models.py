from django.db import models
from django.urls import reverse

#maneger

class Produtos_manager(models.Manager):
    def pesquisa(self,query):
        return Produtos.objects.filter(models.Q(nome__icontains = query),models.Q(descrição__icontains = query)).all()

# Create your models here.
class Produtos(models.Model):
    nome = models.CharField('Nome do Produto',max_length=100,blank=False,null=False,unique=True)
    slug = models.SlugField('Atalho')
    preço = models.FloatField("Preço do produto",blank=False,null=False)
    descrição = models.TextField('Descrição do produto',blank=True,null=False)
    imagem = models.ImageField(upload_to='produto/imagem',verbose_name='Imagem do produto',blank=True)
    
    objects = Produtos_manager()
    
    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ("-preço",)
        
    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse("eclipse:produto", kwargs={"slug": self.slug})
    