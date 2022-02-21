from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from decimal import Decimal
from django.db.models.signals import pre_save, post_save, m2m_changed

from products.models import Product

# Create your models here.

User = get_user_model()

class CartManager(models.Manager):
    def new(self, request):
        return self.model.objects.create(user=request.user)

    def user_cart(self, request):
        return self.model.objects.filter(email=request.user)
    
    def get_cart_or_create_cart(self, request):
        qs = self.model.objects.filter(user=request.user)
        if qs.exists():
            obj = qs.first()
        else:
            obj = self.model.objects.create(user=request.user)
        return obj

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)
    tax = models.DecimalField(default=10.00, max_digits=100, decimal_places=2)
    shipping_charge = models.DecimalField(default=100.00, max_digits=100, decimal_places=2)
    subtotal = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = CartManager()

    def __str__(self):
        return f'{self.user.email} | ${self.total}'

def m2m_changed_cart_receiver(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        products = instance.products.all()
        total = 0
        for x in products:
            total += x.price
        if instance.subtotal != total:
            instance.subtotal = total
            instance.save()

m2m_changed.connect(m2m_changed_cart_receiver, sender=Cart.products.through)

def pre_save_cart_receiver(sender, instance, *args, **kwargs):
    if instance.subtotal > 0:
        tax = 1 + (instance.tax / 100)
        instance.total = (Decimal(instance.subtotal) * Decimal(tax)) + Decimal(instance.shipping_charge)
    else:
        instance.total = 0.00

pre_save.connect(pre_save_cart_receiver, sender=Cart)