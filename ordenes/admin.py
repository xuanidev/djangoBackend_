from django.contrib import admin
from .models import Order, OrderItem

class OrderAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ['id', 'customer', 'status', 'total_amount', 'created_at']
    search_fields = ['customer__user__username', 'status']
    readonly_fields = ['created_at', 'updated_at']

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'product', 'quantity']
    # Fields to search in the list view
    search_fields = ['order__id', 'product__name']

    # Optionally, override form to make fields read-only after creation
    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editing an existing object
            return ['order', 'product'] + list(self.readonly_fields)
        return self.readonly_fields

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
