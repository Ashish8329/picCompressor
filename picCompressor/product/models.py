from django.db import models
from base.base_models import BaseModel
from base.choices import Status
from django.utils.translation import gettext_lazy as _
import uuid

class Product(BaseModel):
    name = models.CharField(
        max_length=255,
        verbose_name=_("Product Name"),
        help_text=_("Enter the name of the product."),
    )  
    sr_no = models.IntegerField(
        verbose_name=_("Serial Number"),
        help_text=_("Unique serial number of the product."),
    )
    status = models.CharField(
        max_length=20,
        choices=[(x.value) for x in Status],
        default=Status.PENDING,
        verbose_name=_("Status"),
        help_text=_("Current status of the product img Processing."),
    )
    
    def __str__(self):
        return f"{self.name} - {self.status}"


class Image(BaseModel):
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE, 
        related_name="images",
        verbose_name=_("Product"),
        help_text=_("Select the product this image belongs to."),
    )
    status = models.CharField(
        max_length=20, 
        choices=[(x.value) for x in Status], 
        default=Status.PENDING,
        verbose_name=_("Status"),
        help_text=_("Processing status of the image."),
    )
    processing_time = models.IntegerField(
        null=True,   
        blank=True,   
        verbose_name=_("Processing Time (seconds)"),
        help_text=_("Time taken to process the image in seconds."),
    )
    image_size_before = models.IntegerField(
        null=True,
        blank=True,
        verbose_name=_("Image Size Before (KB)"),
        help_text=_("Size of the image before compression in kilobytes."),
    )
    image_size_after = models.IntegerField(
        null=True,
        blank=True,
        verbose_name=_("Image Size After (KB)"),
        help_text=_("Size of the image after compression in kilobytes."),
    )
    image_quality = models.IntegerField(
        null=True,
        blank=True,
        verbose_name=_("Image Quality (%)"),
        help_text=_("Quality percentage of the compressed image."),
    )
    original_image = models.ImageField(
        upload_to="original_images/",
        verbose_name=_("Original Image"),
        help_text=_("Upload the original uncompressed image."),
    )
    compressed_image = models.ImageField(
        upload_to="compressed_images/", 
        null=True, 
        blank=True,
        verbose_name=_("Compressed Image"),
        help_text=_("Upload the compressed version of the image."),
    )

    def __str__(self):
        return f"Image {self.id} - {self.status}"
