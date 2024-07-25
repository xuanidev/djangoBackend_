from django.contrib import admin
from .models import Cliente

class UserProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Cliente, UserProfileAdmin)