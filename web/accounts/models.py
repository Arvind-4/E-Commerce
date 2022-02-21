import uuid
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, 
    BaseUserManager,
)

class MyAccountManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must have an Emaill address")
        user  = self.model(
                email=self.normalize_email(email),
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
                email=self.normalize_email(email),
                password=password,
            )
        user.is_admin = True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    id = models.UUIDField(
        default=uuid.uuid4, 
        primary_key=True, 
        editable=False, 
        unique=True
    )
    email = models.EmailField(max_length=60, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = MyAccountManager()

    def __str__(self):
        return f'{self.email} | {self.id}'

    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self, app_label):
        return True
