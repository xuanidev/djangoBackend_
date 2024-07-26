from django.db import models
from clientes.models import Cliente
from productos.models import Product

class Order(models.Model):
    EUR = 'EUR'
    USD = 'USD'
    GBP = 'GBP'
    CURRENCY_CHOICES = [
        (EUR, 'Euro'),
        (USD, 'Dollar'),
        (GBP, 'Pound'),
    ]
    PENDING = 'pending'
    SHIPPED = 'shipped'
    DELIVERED = 'delivered'
    CANCELLED = 'cancelled'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (SHIPPED, 'Shipped'),
        (DELIVERED, 'Delivered'),
        (CANCELLED, 'Cancelled'),
    ]

    customer = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(
        max_length=3,
        choices=CURRENCY_CHOICES,
        default=EUR,
    )

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"Order {self.id}"

    def save(self, *args, **kwargs):
        if self.pk is not None:
            # Check if the instance already exists in the database
            original = Order.objects.get(pk=self.pk)
            if original.customer != self.customer:
                raise ValueError("Cannot change the customer associated with this order.")
        super().save(*args, **kwargs)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    customization_details = models.JSONField(null=True, blank=True)

    class Meta:
        verbose_name = "Order Item"
        verbose_name_plural = "Order Items"

    def __str__(self):
        return f"Item {self.id}"

    def save(self, *args, **kwargs):
        if self.pk is not None:
            # Check if the instance already exists in the database
            original = OrderItem.objects.get(pk=self.pk)
            if original.order != self.order:
                raise ValueError("Cannot change the order associated with this order item.")
        super().save(*args, **kwargs)