from django.urls import path

from .api import CategoryListView, ProductCategoryView

urlpatterns = [
    path('list/', CategoryListView.as_view()),
    path('product-filter/<str:slug>/', ProductCategoryView.as_view()),
]