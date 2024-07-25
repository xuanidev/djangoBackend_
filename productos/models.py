from django.db import models
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    link_of_nfc = models.URLField(max_length=500, blank=True, null=True)
    personalization_image = models.ImageField(upload_to='personalization_images/', blank=True, null=True)
    personalization_document = models.FileField(upload_to='personalization_docs/', blank=True, null=True)
    available_products = models.JSONField(null=True, blank=True)
    options = models.JSONField(null=True, blank=True)
    dimensions = models.CharField(max_length=100, blank=True, null=True)
    mainImg = models.URLField()
    imgsProduct = models.JSONField()
    availables = models.IntegerField()
    puntuation = models.IntegerField(default=0)

    def __str__(self):
        return self.name
