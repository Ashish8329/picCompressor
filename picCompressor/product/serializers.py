from rest_framework import serializers
from .models import Product, Image

class ProductSerializer(serializers.ModelSerializer):
    csv_file = serializers.FileField(required=True)
    class Meta:
        model = Product
        fields = '__all__'