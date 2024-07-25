# views.py
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status

from clientes.models import Cliente
from clientes.serializers import ClienteSerializer
from .serializers import UserSerializer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])

    if not user.check_password(request.data['password']):
        return Response({"error": "Invalid password"}, status=status.HTTP_400_BAD_REQUEST)
    
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)

    return Response({"token": token.key, "user": serializer.data}, status=status.HTTP_200_OK)


@api_view(['POST'])
def register(request):
    user_data = request.data.copy()
    user_serializer = UserSerializer(data=user_data)

    if user_serializer.is_valid():
        # Crear el usuario
        user = user_serializer.save()
        
        # Crear un token para el usuario
        token = Token.objects.create(user=user)
        
        # Crear los datos del cliente, usando el email del usuario
        cliente_data = {
            "email": user.email,  # Usa el email del usuario para el cliente
            "first_name": user_data.get('first_name', ''),
            "middle_name": user_data.get('middle_name', ''),
            "last_name": user_data.get('last_name', ''),
            "phone": user_data.get('phone', ''),
            "address_line1": user_data.get('address_line1', ''),
            "address_line2": user_data.get('address_line2', ''),
            "city": user_data.get('city', ''),
            "state": user_data.get('state', ''),
            "postcode": user_data.get('postcode', ''),
            "country": user_data.get('country', ''),
        }

        # Crear el cliente con los datos proporcionados
        cliente_serializer = ClienteSerializer(data=cliente_data)

        if cliente_serializer.is_valid():
            # Guardar el cliente y asociar el usuario creado
            cliente = cliente_serializer.save(user=user)
        else:
            # Si la creación del cliente falla, eliminar el usuario creado y responder con error
            user.delete()
            return Response(cliente_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({'token': token.key, "user": user_serializer.data}, status=status.HTTP_201_CREATED)
    
    return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    serializer = UserSerializer(instance=request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)
