from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, OrderDetailView, OrderItemViewSet

router = DefaultRouter()
router.register(r'', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('<int:order_id>/', OrderDetailView.as_view(), name='order-detail'),
    path('<int:order_id>/items/', OrderItemViewSet.as_view({'get': 'list', 'post': 'create'}), name='orderitem-list'),
    path('<int:order_id>/items/<int:pk>/', OrderItemViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='orderitem-detail'),
]
