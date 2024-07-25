# clientes/urls.py
from django.urls import path
from .views import ClienteViewSet, ClienteDetailView

urlpatterns = [
    # For CRUD operations using ModelViewSet (assuming you're using a router)
    path('', ClienteViewSet.as_view({'get': 'list', 'post': 'create'}), name='cliente-list'),
    path('clientes/<int:pk>/', ClienteDetailView.as_view(), name='cliente-detail'),
]
