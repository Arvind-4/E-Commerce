from django.contrib import admin

from .models import Checkout

# Register your models here.

class CheckoutAdmin(admin.ModelAdmin):
    list_display = ['user', 'updated', 'timestamp']

admin.site.register(Checkout, CheckoutAdmin)