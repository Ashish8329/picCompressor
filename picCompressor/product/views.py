from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from  rest_framework import viewsets
from .models import Product, Image
from .serializers import ProductSerializer

class ProdcutViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

