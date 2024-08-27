from django.urls import path
from .views import ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView, StockListCreateAPIView, StockRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),
    path('stocks/', StockListCreateAPIView.as_view(), name='stock-list-create'),
    path('stocks/<int:pk>/', StockRetrieveUpdateDestroyAPIView.as_view(), name='stock-detail'),
]
