from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from  rest_framework import viewsets
from .models import Product, Image
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status

class ProdcutViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
         
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)   
        product = serializer.save()  
        
        return Response({"req_id": product.req_id}, status=status.HTTP_201_CREATED)

