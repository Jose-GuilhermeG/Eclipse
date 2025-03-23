from django.db import models
from django.urls import reverse

#maneger

class Produtos_manager(models.Manager):
    def pesquisa(self,query):
        return Produtos.objects.filter(nome__icontains = query).all()
    
    def pegar_categorias_produtos_id(self,query):
        return Categorias_Produtos.objects.filter(produto = query)
    
    #resolvendo o n+1 problem
    def pegar_produtos_por_categoria(self,query):
        categoria = Categorias.objects.filter(nome__icontains=query).first()
        if categoria:
            return Produtos.objects.prefetch_related('categorias').filter(categorias = categoria)
        return []

# Create your models here.
class Produtos(models.Model):
    nome = models.CharField('Nome do Produto',max_length=100,blank=False,null=False,unique=True)
    slug = models.SlugField('Atalho')
    preço = models.FloatField("Preço do produto",blank=False,null=False)
    descrição = models.TextField('Descrição do produto',blank=True,null=False)
    imagem = models.ImageField(upload_to='produto/imagem',verbose_name='Imagem do produto',blank=True)
    categorias = models.ManyToManyField('Categorias',through="Categorias_Produtos",verbose_name="Categorias do produto",blank=True)
    
    objects = Produtos_manager()
    
    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ("-preço",)
        
    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse("eclipse:produto", kwargs={"slug": self.slug})
    
    def pegar_categorias(self):
        return Produtos.objects.pegar_categorias_produtos_id(self.id)
    
    def pegar_versões(self):
        return Variantes.objects.filter(produto=self.id)
    
class Categorias(models.Model):
    nome = models.CharField('nome categoria',unique=True,max_length=100,blank=False,null=False)
    slug = models.SlugField("Atalho")
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = 'Categorias'
        
    def __str__(self):
        return self.nome
    
class Categorias_Produtos(models.Model):
    produto = models.ForeignKey(Produtos,null=False,blank=False,verbose_name='Produto',on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categorias,null=False,blank=False,verbose_name='Categoria',on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Categoria produto"
        verbose_name_plural = 'Categorias do produto'
        
    def __str__(self):
        return f'{self.produto} - {self.categoria}'
    
class Variantes(models.Model):
    produto = models.ForeignKey(Produtos,on_delete=models.CASCADE,verbose_name='Produto principal')
    nome = models.CharField("Nome da variante",max_length=100,unique=True,blank=False,null=False)
    descrição = models.CharField("Breve Descrição da variante",max_length=100,blank=True)
    sobre = models.TextField("Tudo sobre a variante",blank=True)
    preço = models.FloatField("Preço da variante",blank=False)
    imagem = models.ImageField('Imagem da variante',upload_to='produto/versões',blank=True)

    class Meta:
        verbose_name = 'Versão'
        verbose_name_plural = 'Versões'
        
    def __str__(self):
        return f'{self.produto} - {self.nome}'