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

from time import sleep

class ProdutosAllApi(APIView):
    def get(self, request) :
        quantia = request.GET.get('quantia',100)
        nome_filter = request.GET.get("nome",False)
        promoção_hj = request.GET.get("promoção_hj",False)
        
        if nome_filter:
            produtos = Produtos.objects.filter(Nome__icontains = nome_filter)
        elif promoção_hj:
            produtos = Promoção.objects.all()
            s = []
            for item in produtos:
                print(item.Produto)
                s.append(ProdutosSerializers(Produtos.objects.get(Nome = item.Produto)).data)
            return Response(s)
            
        else:
            produtos = Produtos.objects.all()
        produtos_quantia = produtos[:int(quantia)]
        produtosSerializers_var = ProdutosSerializers(produtos_quantia, many = True)
        return Response(produtosSerializers_var.data)

@api_view(['GET'])
def Pesquisa_produto(request):
        pesquisa = request.GET.get("pesquisa",False)
        produtos_encontrados = Produtos.objects.filter(Nome__icontains = pesquisa).all()
        if produtos_encontrados:
            produto_result = ProdutosSerializers(produtos_encontrados,many = True)
            response = Response(produto_result.data)
            
            return response
        
        return Response('nenhum produto encontrado',status = status.HTTP_204_NO_CONTENT)

class Pesquisa_produto_view(View):
    def get(self,request,pesquisa):
        produtos = Produtos.objects.filter(Nome__icontains = pesquisa).all()
        context = {'produtos' : produtos}
        return render(request,'pesquisa_page.html',context=context)
    
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