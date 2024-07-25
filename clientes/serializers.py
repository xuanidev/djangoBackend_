from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['first_name', 'middle_name', 'last_name', 'email', 'phone', 'address_line1', 'address_line2', 'city', 'state', 'postcode', 'country']
        extra_kwargs = {
            'first_name': {'required': False},
            'middle_name': {'required': False},
            'last_name': {'required': False},
            'email': {'required': False},
            'phone': {'required': False},
            'address_line1': {'required': False},
            'address_line2': {'required': False},
            'city': {'required': False},
            'state': {'required': False},
            'postcode': {'required': False},
            'country': {'required': False},
        }
