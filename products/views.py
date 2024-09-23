from rest_framework import viewsets

from products.models import Product
from products.serializers import ProductsSerializer


class ProductsViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Employee model
    """
    serializer_class = ProductsSerializer
    queryset = Product.objects.all()
