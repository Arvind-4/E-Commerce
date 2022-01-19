from urllib import request
from carts.models import Cart
from rest_framework.generics import ListAPIView

from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import permissions

from .serializers import CartSerializer
from products.models import Product
from django.conf import settings

User = settings.AUTH_USER_MODEL

class CartListView(ListAPIView):
    serializer_class = CartSerializer
    def get_queryset(self, *args, **kwargs):
        qs = Cart.objects.filter(user=self.request.user)
        if qs.exists():
            obj = qs
        else:
            obj = []
        return obj


class CartAddProducts(ListAPIView, LoginRequiredMixin):
    serializer_class = CartSerializer
        
    def get_queryset(self, *args, **kwargs):
        request = self.request
        product_id = self.kwargs.get('id')
        product_obj = Product.objects.filter(id=product_id)
        if not product_obj.exists():
            raise Http404
        else:
            product_obj = product_obj.first()
        qs = Product.objects.filter(id=product_id)
        cart_obj = Cart.objects.get_cart_or_create_cart(request=request)
        if product_obj.id in [x.id for x in qs]:
            cart_obj.products.add(product_obj)
        else:
            print('Alreay exists!')
        user_qs = Cart.objects.filter(user=request.user)
        return user_qs

class CartRemoveProducts(ListAPIView, LoginRequiredMixin):
    serializer_class = CartSerializer
    def get_queryset(self, *args, **kwargs):
        # request = self.request
        # slug = self.kwargs.get('slug')
        # product_obj = Product.objects.get(slug=slug)
        # qs = Product.objects.filter(slug=slug)

        # cart_obj = Cart.objects.filter(user__email=request.user)
        # if cart_obj.exists():
        #     qs_cart = cart_obj.first()
        # else:
        #     qs_cart = Cart.objects.new(request=request)

        # if product_obj.slug in [x.slug for x in qs]:
        #     qs_cart.products.remove(product_obj)
        # user_qs = Cart.objects.filter(user=request.user)
        # return user_qs
        request = self.request
        product_id = self.kwargs.get('id')
        product_obj = Product.objects.filter(id=product_id)
        if not product_obj.exists():
            raise Http404
        else:
            product_obj = product_obj.first()
        qs = Product.objects.filter(id=product_id)
        cart_obj = Cart.objects.get_cart_or_create_cart(request=request)
        if product_obj.id in [x.id for x in qs]:
            cart_obj.products.remove(product_obj)
        else:
            print('Alreay exists!')
        user_qs = Cart.objects.filter(user=request.user)
        return user_qs