from django.db import models
from django.contrib.auth import get_user_model
from django_countries import countries

COUNTRY_CHOICES = tuple(countries)

User = get_user_model()

# Create your models here.

class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    number = models.IntegerField()
    zip_code = models.IntegerField()
    country = models.CharField(choices=COUNTRY_CHOICES, max_length=100)

    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}|{self.email}'
