from django.urls import path, include
from .views import ProdcutViewSet

urlpatterns = [
    path('product/', ProdcutViewSet.as_view({'get':"list", 'post':'create'}), name="my-view")
]