from rest_framework import serializers

from .models import Image, Product
from .utils import validate_csv_file


class ProductSerializer(serializers.ModelSerializer):
    csv_file = serializers.FileField(required=True)

    class Meta:
        model = Product
        fields = "__all__"

    def validate(self, attrs):
        csv_file = attrs.get("csv_file")
        validate_csv_file(csv_file)
        return super().validate(attrs)


class ImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"
