from rest_framework import serializers
from .models import Product, Stock, StockProduct

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description']

class StockProductSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()

    class Meta:
        model = StockProduct
        fields = ['product', 'price']

class StockSerializer(serializers.ModelSerializer):
    stock_products = StockProductSerializer(many=True, read_only=True)

    class Meta:
        model = Stock
        fields = ['id', 'name', 'address', 'stock_products']
