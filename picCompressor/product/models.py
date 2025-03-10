import uuid
from io import BytesIO

from django.core.exceptions import ValidationError
from django.core.files.base import ContentFile
from django.db import models
from django.utils.translation import gettext_lazy as _
from PIL import Image as PILImage

from base.base_models import BaseModel
from base.choices import Status
from base.utils import generate_short_uuid


class Product(BaseModel):
    req_id = models.CharField(
        max_length=50, unique=True, editable=False, default=generate_short_uuid
    )
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
        max_length=100,
        choices=[(x.value) for x in Status],
        default=Status.PENDING,
        verbose_name=_("Status"),
        help_text=_("Current status of the product img Processing."),
    )
    csv_file = models.FileField(
        upload_to="csv_file/",
        null=True,
        blank=True,
        verbose_name=_("CSV file"),
        help_text=_("product csv file"),
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
        max_length=100,
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

    def compress_image(self):
        """Compress the image by 50% and save it in `compressed_image` field."""
        if not self.original_image:
            return

        try:
            img = PILImage.open(self.original_image)
            img = img.convert("RGB")  # Ensure compatibility (PNG, WebP, etc.)

            # **Step 1: Resize image to 50% of original size**
            width, height = img.size
            new_size = (width // 2, height // 2)  # Reduce to 50%
            img = img.resize(new_size, PILImage.LANCZOS)

            # **Step 2: Save image with compression (quality=50)**
            img_io = BytesIO()
            img.save(img_io, format="JPEG", quality=50)  # JPEG format, 50% quality
            img_io.seek(0)

            # **Step 3: Save compressed image**
            compressed_filename = (
                f"compressed_{self.original_image.name.split('/')[-1]}"
            )
            self.compressed_image.save(
                compressed_filename, ContentFile(img_io.read()), save=False
            )

            # **Step 4: Update size info**
            self.image_size_after = self.compressed_image.size // 1024  # KB
            self.status = Status.COMPLETED.value[0]  
        except PILImage.UnidentifiedImageError:
            raise ValidationError(
                "Invalid image format. Please upload a valid image file."
            )

        except Exception as e:
            raise ValidationError(f"Image compression failed: {str(e)}")

    def save(self, *args, **kwargs):
        """Override save method to compress image before saving."""
        if not self.compressed_image:  # Only compress if not already compressed
            self.compress_image()
        super().save(*args, **kwargs)
