#django imports
from django.shortcuts import render
from django.views import View

#restframework imports
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

#serializers imports
from .serializers import ProdutosSerializers

#models
from .models import Produtos

# Create your views here.
class Index(View):
    def get(self, request) :
        return render(request, "index.html")
    
class ProdutosAllApi(APIView):
    def get(self, request,quantia) :
        produtos_quantia = Produtos.objects.all()[:quantia]
        produtosSerializers_var = ProdutosSerializers(produtos_quantia, many = True)
        return Response(produtosSerializers_var.data)
    