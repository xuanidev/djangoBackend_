# views.py
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Cliente
from .serializers import ClienteSerializer

# Function-based detail view using APIView for Cliente
class ClienteDetailView(APIView):
    permission_classes = (IsAuthenticated,)  # Ensure the user is authenticated

    def get(self, request, cliente_id):
        cliente = get_object_or_404(Cliente, id=cliente_id)
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)

    def put(self, request, cliente_id):
        cliente = get_object_or_404(Cliente, id=cliente_id)
        serializer = ClienteSerializer(cliente, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, cliente_id):
        cliente = get_object_or_404(Cliente, id=cliente_id)
        cliente.delete()
        return Response(status=204)

# ModelViewSet for CRUD operations for Cliente
class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()
    permission_classes = (IsAuthenticated,)  # Ensure the user is authenticated
