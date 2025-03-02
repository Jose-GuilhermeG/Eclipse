#django imports
from django.shortcuts import render,redirect
from django.views import View
from django.http.response import HttpResponseNotFound
from django.db.models import Q
from django.views.generic import ListView
#restframework imports
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

#serializers imports
from .serializers import ProdutosSerializers,PromoçãoSerializers

#models
from .models import Produtos,Produto_Cor,Categorias,Promoção

#jwt
from account.utils.jwt import pegar_user_jwt

# Create your views here.
def Index(request):
    return render(request, "index.html",context={'user' : pegar_user_jwt(request)})
    
class ProdutosView(View):
    def get(self,request,nome):
        try:
            produto_consult = Produtos.objects.get(Nome=nome)
            cores_produtos = Produto_Cor.objects.filter(Produto = produto_consult).all()
            context = {'produto' : produto_consult,'cores' : cores_produtos}
            return render(request, "produto.html",context=context)
        except Produtos.DoesNotExist:
            return HttpResponseNotFound()


class ProdutosAllApi(APIView):
    def get(self, request) :
        quantia = request.GET.get('quantia',100)
        nome_filter = request.GET.get("nome",False)
        promoção_hj = request.GET.get("promoção_hj",False)
        id_pedido = request.GET.get("id",False)
        
        many = True
        
        if nome_filter:
            produtos = Produtos.objects.filter(Nome__icontains = nome_filter)
        elif id_pedido:
            produtos = Produtos.objects.get(id=id_pedido)
            many = False
        elif promoção_hj:
            produtos = Promoção.objects.all()
            s = []
            for item in produtos:
                s.append(ProdutosSerializers(Produtos.objects.get(Nome = item.Produto)).data)
            return Response(s)
            
        else:
            produtos = Produtos.objects.all()
            
        if many:
            produtos_quantia = produtos[:int(quantia)]
        else:
            produtos_quantia = produtos
        produtosSerializers_var = ProdutosSerializers(produtos_quantia, many = many)
        return Response(produtosSerializers_var.data)
    
class FilterProdutos(View):
    def get(self,request):
        categoria = request.GET.get("categoria")
        preço = request.GET.get("preço")
        produtos = Produtos.objects.filter(Categoria=categoria).all()
        lista = []
        for produto in produtos:
            lista.append(produto)
        if preço.upper() == 'MENOR':
            for item in range(len(lista)):
                for item in range(len(lista)):
                    if item < len(lista) - 1 :
                        if lista[item].Preço > lista[item+1].Preço:
                            lista[item],lista[item+1] = lista[item+1],lista[item]
        else:
            for item in range(len(lista)):
                for item in range(len(lista)):
                    if item < len(lista) - 1 :
                        if lista[item].Preço < lista[item+1].Preço:
                            lista[item+1],lista[item] = lista[item],lista[item+1]
                        
        return render(request,'filter.html',context={"produtos":lista})

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
        
class Sobre(View):
    def get(self,request):
        return render(request, "sobre.html")