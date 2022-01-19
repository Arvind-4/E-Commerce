from django.urls import path

from .views import (
    signin_view,
    signup_view,
    signout_view,
)

urlpatterns = [
    path('sign-in/', signin_view, name='sign-in'),
    path('sign-up/', signup_view, name='sign-up'),
    path('sign-out/', signout_view, name='sign-out'),
]