from django.db import models


# Create your models here.
class Product(models.Model):
    # Currency choices
    EUR = 'EUR'
    USD = 'USD'
    GBP = 'GBP'
    CURRENCY_CHOICES = [
        (EUR, 'Euro'),
        (USD, 'Dollar'),
        (GBP, 'Pound'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    mainImg = models.URLField()
    imgsProduct = models.JSONField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availables = models.IntegerField()
    currency = models.CharField(
        max_length=3,
        choices=CURRENCY_CHOICES,
        default=EUR,
    )
    puntuation = models.IntegerField(default=0)

    def __str__(self):
        return self.name
