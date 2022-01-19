from category.models import Category
from django.http import Http404
from rest_framework.generics import ListAPIView

from django.shortcuts import redirect
from products.models import Product
from products.api.serializers import ProductSerializer

from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes

from .serializers import CategorySerializer

@permission_classes((AllowAny, ))
class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

@permission_classes((AllowAny, ))
class ProductCategoryView(ListAPIView):
    # queryset = Product.objects.filter(category__category=)
    def get_queryset(self, *args, **kwargs):
        slug = self.kwargs['slug']
        qs = Product.objects.filter(category__slug=slug)
        if qs.exists():
            return qs
        else:
            return Http404
    serializer_class = ProductSerializer