from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Stock(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class StockProduct(models.Model):
    stock = models.ForeignKey(Stock, related_name='stock_products', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='stock_products', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} at {self.stock.name}"
