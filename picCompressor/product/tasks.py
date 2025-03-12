# tasks.py
import time
import uuid
from io import BytesIO
from time import sleep

import requests
from celery import shared_task
from django.conf import settings
from django.core.files.base import ContentFile
from PIL import Image as PILImage

from base.choices import Status

WEBHOOK_URL = f"{settings.SITE_URL}/update_status_webhook/"


def trigger_webhook(product):
    """Triggers a webhook when all images of a product are processed."""
    payload = {
        "product_id": product.id,
        "status": Status.COMPLETED.value[0],
        "message": "All images processed successfully.",
    }
    try:
        response = requests.post(WEBHOOK_URL, json=payload)
        response.raise_for_status()
        return f"Webhook triggered for Product {product.id}."
    except requests.RequestException as e:
        return f"Webhook trigger failed: {str(e)}"


@shared_task
def process_image(image_id):
    """Celery task to compress image asynchronously."""
    from .models import Image

    sleep(2)
    image = Image.objects.get(id=image_id)

    if not image.original_image:
        return "No image found."

    try:
        img = PILImage.open(image.original_image)
        img = img.convert("RGB")  # Ensure compatibility

        # Step 1: Resize image (50% reduction)
        width, height = img.size
        new_size = (width // 2, height // 2)
        img = img.resize(new_size, PILImage.LANCZOS)

        # Step 2: Save image with compression
        img_io = BytesIO()
        img.save(img_io, format="JPEG", quality=50)  # JPEG, 50% quality
        img_io.seek(0)

        # Step 3: Save compressed image
        compressed_filename = f"compressed_{uuid.uuid4().hex}.jpg"
        image.compressed_image.save(
            compressed_filename, ContentFile(img_io.read()), save=False
        )

        # Step 4: Update metadata
        image.image_size_after = image.compressed_image.size // 1024  # KB
        image.status = Status.COMPLETED.value[0]

        image.save()

        # weebhook trigger
        product = image.product

        if not Image.objects.filter(
            product_id=product.id, status=Status.PENDING.value[0]
        ).exists():
            return trigger_webhook(product)

        return f"Image {image.id} processed successfully."

    except PILImage.UnidentifiedImageError:
        return f"Invalid image format for image {image.id}."

    except Exception as e:
        return f"Image processing failed: {str(e)}"
