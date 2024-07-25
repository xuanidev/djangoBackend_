# views.py
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializers import ProductSerializer

# Function-based detail view using APIView
class ProductDetailView(APIView):
    permission_classes = (IsAuthenticated,)  # Ensure the user is authenticated

    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

# ModelViewSet for CRUD operations
class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = (IsAuthenticated,)  # Ensure the user is authenticated
