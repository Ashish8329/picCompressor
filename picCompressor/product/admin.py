from django.contrib import admin
from base.base_admin import BaseAdmin
from .models import Product, Image

@admin.register(Product)
class ProductAdmin(BaseAdmin):
    fields = [
        "name",
        "sr_no",
        "status",
    ]
    list_display = [
        "name",
        "status",
    ]

    def save_model(self, request, obj, form, change):
        return super().save_model(request, obj, form, change)

@admin.register(Image)
class ImageAdmin(BaseAdmin):
    fields = [
        "product",
        "status",
        "processing_time",
        "image_size_before",
        "image_size_after",
        "image_quality",
        "original_image",
        "compressed_image",
    ]
    readonly_fields = [
        "processing_time",
        "image_size_before",
        "image_size_after",
    ]
    list_display = [
        "product",
        "status",
        "processing_time",
    ]

    def save_model(self, request, obj, form, change):
        return super().save_model(request, obj, form, change)