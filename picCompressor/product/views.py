from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Image, Product
from .serializers import ProductSerializer
from .utils import process_images


class ProdcutViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):

        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = serializer.save()

        process_images(product.csv_file, product)  # TODO async
        return Response({"req_id": product.req_id}, status=status.HTTP_201_CREATED)
