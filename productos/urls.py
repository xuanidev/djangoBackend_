# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductDetailView, ProductViewSet

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('product/<int:product_id>/', ProductDetailView.as_view(), name='product_detail'),
    path('', include(router.urls)),
]
