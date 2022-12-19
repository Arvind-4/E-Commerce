from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Account

# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'date_joined',
        'last_login',
        'is_superuser',
    )
    list_filter = ("email",)
    search_fields = ("email", "is_superuser")
    ordering = ("-date_joined", "-last_login")

admin.site.unregister(Group)
admin.site.register(Account, AccountAdmin)