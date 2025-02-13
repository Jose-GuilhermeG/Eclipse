#django imports
from django.shortcuts import render
from django.views import View
from django.http.response import HttpResponseNotFound
from django.db.models import Q

#restframework imports
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

#serializers imports
from .serializers import ProdutosSerializers,PromoçãoSerializers

#models
from .models import Produtos,Produto_Cor,Categorias,Promoção

# Create your views here.
def Index(request):
    return render(request, "index.html")
    
class ProdutosView(View):
    def get(self,request,nome):
        try:
            produto_consult = Produtos.objects.get(Nome=nome)
            print(produto_consult.desconto())
            cores_produtos = Produto_Cor.objects.filter(Produto = produto_consult).all()
            context = {'produto' : produto_consult,'cores' : cores_produtos}
            return render(request, "produto.html",context=context)
        except Produtos.DoesNotExist:
            return HttpResponseNotFound()
    
class ProdutosAllApi(APIView):
    def get(self, request,quantia) :
        produtos_quantia = Produtos.objects.all()[:quantia]
        produtosSerializers_var = ProdutosSerializers(produtos_quantia, many = True)
        return Response(produtosSerializers_var.data)

@api_view(['GET'])
def Pesquisa_produto(request,pesquisa):
        produtos_encontrados = Produtos.objects.filter(Nome__icontains = pesquisa).all()
        if produtos_encontrados:
            produto_result = ProdutosSerializers(produtos_encontrados,many = True)
            response = Response(produto_result.data)
            
            return response
        
        return Response('nenhum produto encontrado',status = status.HTTP_204_NO_CONTENT)
    
class ProdutosCategoriasView(View):
    def get(self, request,categoria):
        try:
            categorai_escolhida = getattr(Categorias, categoria.upper()).value
            produtos = Produtos.objects.filter(Categoria = categorai_escolhida ).all()
            context = {"produtos":produtos}
            return render(request, "categorias.html",context=context)
        except AttributeError:
            return HttpResponseNotFound()
        
class ProdutoExpecificoApi(APIView):
    def get(self,request,nome):
        try:
            produto = Produtos.objects.get(Nome = nome)
            response = Response(ProdutosSerializers(produto).data)
            return response
        except Produtos.DoesNotExist:
            return HttpResponseNotFound()