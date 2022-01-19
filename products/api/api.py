from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers
from django.http import Http404

from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes

from products.models import Product

from .serializers import ProductSerializer


# Create your views here.

# class ProductCreate(CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

@permission_classes((AllowAny, ))
class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# class ProductUpdate(RetrieveUpdateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = 'slug'

# class ProductDelete(DestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = 'slug'

# @permission_classes((AllowAny, ))
# class ProductDetail(APIView):
#     def get_object(self, slug):
#         try:
#             return Product.objects.filter(slug=slug).first()
#         except:
#             raise Http404
    
#     def get(self, request, slug, format=None, *args, **kwargs):
#         instance = self.get_object(slug)
#         if instance:
#             obj = ProductSerializer(instance)
#             return Response(obj.data)
#         else:
#             return Http404

@permission_classes((AllowAny, ))
class ProductDetail(RetrieveAPIView):
    serializer_class = ProductSerializer
    lookup_field = ['slug', 'id']
    def get_object(self):
        slug = self.kwargs.get('slug')
        id_ = self.kwargs.get('id')
        product_qs = Product.objects.filter(slug=slug, id=id_)
        if not product_qs.exists():
            raise Http404
        return product_qs.first()
        
