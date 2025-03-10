import csv
import io
from time import time

import requests
from django.core.files.base import ContentFile
from rest_framework import serializers

from base.choices import Status

from .models import Image, Product


def decode_csv_file(csv_file):
    """Decodes an uploaded CSV file and returns a file-like object"""
    try:
        # Ensure the uploaded file is a CSV
        if not csv_file.name.endswith(".csv"):
            raise ValueError("Uploaded file must be a CSV.")

        # Read and decode file (from bytes to string)
        decoded_file = csv_file.read().decode("utf-8")

        # Convert string to file-like object for CSV reader
        return io.StringIO(decoded_file)

    except (ValueError, UnicodeDecodeError) as e:
        raise serializers.ValidationError({"csv_file": str(e)})


def validate_csv_file(csv_file):
    """Validates the uploaded CSV file and returns the number of records"""
    try:
        file_io = decode_csv_file(csv_file)  # ✅ Reusing the decode function

        reader = csv.reader(file_io)
        header = next(reader, None)  # Read the first row (header)

        if header is None or len(header) != 2:
            raise ValueError(
                "Error: handling CSV data, make sure the CSV data is in the provided format."
            )

        # # Count the number of records (excluding the header) #TODO
        # record_count = sum(1 for _ in reader)

        # return record_count  # Returning the number of records

    except (ValueError, UnicodeDecodeError) as e:
        raise serializers.ValidationError({"csv_file": str(e)})


def process_images(csv_file, product):
    """Processes a CSV file and stores images in the database linked to a given product."""
    file_io = decode_csv_file(csv_file)
    reader = csv.reader(file_io)
    next(reader)  # Skip header row

    errors = []  # Collect errors for better response handling

    for row in reader:
        try:
            if len(row) < 2:
                raise ValueError(
                    "Row has missing columns. Expected: [Product Name, Image URL]."
                )

            product_name, image_url = row
            if not product_name.strip() or not image_url.strip():
                raise ValueError(f"Missing data in row: {row}")

            # Get image content
            start_time = time()
            response = requests.get(image_url, stream=True)
            response.raise_for_status()

            # Extract file extension
            ext = image_url.split(".")[-1].split("?")[0]
            filename = f"{product.name}.{ext}"

            # Calculate original image size (in KB)
            original_size_kb = len(response.content) // 1024

            # Create Image object and save to DB
            image_instance = Image(
                product=product,
                status=Status.PENDING.value,
                image_size_before=original_size_kb,
                processing_time=0,  # Placeholder, updated below
            )
            image_instance.original_image.save(
                filename, ContentFile(response.content), save=True
            )

            # Update processing time
            image_instance.processing_time = int(time() - start_time)
            image_instance.status = Status.COMPLETED.value  # Assuming success
            image_instance.save(update_fields=["processing_time", "status"])

        except requests.RequestException as e:
            errors.append(f"Failed to download {image_url}: {str(e)}")
        except ValueError as e:
            errors.append(str(e))

    if errors:
        raise serializers.ValidationError({"errors": errors})

    return {"message": "All images processed successfully!"}
