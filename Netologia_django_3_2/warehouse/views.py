from rest_framework import generics, filters
from .models import Product, Stock
from .serializers import ProductSerializer, StockSerializer

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']

class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class StockListCreateAPIView(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['stock_products__product__name', 'stock_products__product__description']

class StockRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
