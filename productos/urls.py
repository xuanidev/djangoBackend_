# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, product_detail

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    # Route for the product_detail function-based view
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    
    # Include the router URLs
    path('', include(router.urls)),
]
