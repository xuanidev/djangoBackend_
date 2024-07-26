from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    middle_name = models.CharField(max_length=100, blank=True)  # Optional field
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    address_line1 = models.CharField(max_length=255, blank=True)
    address_line2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    postcode = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username

    @property
    def username(self):
        return self.user.username
    
    @property
    def orders(self):
        return self.order_set.all()

    def save(self, *args, **kwargs):
            if self.pk is not None:
                # The instance already exists, check if the user has been changed
                original = Cliente.objects.get(pk=self.pk)
                if original.user != self.user:
                    raise ValueError("Cannot change the user of a Cliente instance once set.")
            super().save(*args, **kwargs)