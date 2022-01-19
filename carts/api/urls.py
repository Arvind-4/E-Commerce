from django.urls import path

from .api import (
    CartListView,
    CartAddProducts,
    CartRemoveProducts
)

urlpatterns = [
    path('', CartListView.as_view()),
    path('add/<str:slug>/<uuid:id>/', CartAddProducts.as_view()),
    path('remove/<str:slug>/<uuid:id>/', CartRemoveProducts.as_view()),
]