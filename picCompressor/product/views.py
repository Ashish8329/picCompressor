from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from base.choices import Status

from .models import Image, Product
from .serializers import ImageSerializers, ProductSerializer
from .utils import process_images


class ProdcutViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        """
        Retrieve and process images associated with a given request ID.

        """
        req_id = request.GET.get("req_id")

        # Validate if req_id is provided
        if not req_id:
            return Response(
                {"error": "Missing required parameter: req_id"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            images = Image.objects.filter(product__req_id=req_id).values_list(
                "status", "compressed_image"
            )

            if not images.exists():
                return Response(
                    {"error": "No images found for the given request ID"},
                    status=status.HTTP_404_NOT_FOUND,
                )

            total_img_count = len(images)
            compred_img_count = sum(
                1 for status, _ in images if status == Status.COMPLETED.value[0]
            )
            compressed_images_urls = [img_url for _, img_url in images]

            compressed_perc = (
                round((compred_img_count / total_img_count) * 100)
                if total_img_count
                else 0
            )

            response_data = {
                "request_id": req_id,
                "status": Status.PENDING.value[0],
            }

            if compressed_perc == 100:
                response_data["output_image_urls"] = compressed_images_urls
                response_data["status"] = Status.COMPLETED.value[0]

            else:
                response_data["compressed_Perc"] = compressed_perc

            return Response(response_data)

        except ObjectDoesNotExist:
            return Response(
                {"error": "Invalid request ID or associated product does not exist"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        except Exception as e:
            return Response(
                {"error": f"An unexpected error occurred: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = serializer.save()

        process_images(product.csv_file, product)  # TODO async
        return Response({"req_id": product.req_id}, status=status.HTTP_201_CREATED)


class WebhookViewSet(viewsets.ViewSet):
    """Webhook endpoint to update product status when image processing is complete."""

    @action(detail=False, methods=["POST"], url_path="update-status")
    def update_product_status(self, request):
        """Handles webhook requests to update the product status."""
        product_id = request.data.get("product_id")
        new_status = request.data.get("status")

        if not product_id or not new_status:
            return Response(
                {"error": "Missing required fields."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        product = get_object_or_404(Product, id=product_id)
        product.status = new_status
        product.save(update_fields=["status"])

        return Response(
            {"message": f"Product {product_id} status updated successfully."},
            status=status.HTTP_200_OK,
        )
