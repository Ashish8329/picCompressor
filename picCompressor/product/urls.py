from django.urls import include, path

from .views import ProdcutViewSet, WebhookViewSet

urlpatterns = [
    path(
        "product/",
        ProdcutViewSet.as_view({"get": "list", "post": "create"}),
        name="my-view",
    ),
    path(
        "update_status_webhook/",
        WebhookViewSet.as_view({"post": "update_product_status"}),
        name="webhook",
    ),
]
