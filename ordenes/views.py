# views.py
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer

# Function-based detail view using APIView for Order
class OrderDetailView(APIView):
    permission_classes = (IsAuthenticated,)  # Ensure the user is authenticated

    def get(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def put(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        serializer = OrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        order.delete()
        return Response(status=204)

# ModelViewSet for CRUD operations for Order
class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = (IsAuthenticated,)  # Ensure the user is authenticated