from django.contrib import admin
from .models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    readonly_fields = ['user']  # Make the user field read-only in the admin

admin.site.register(Cliente, ClienteAdmin)