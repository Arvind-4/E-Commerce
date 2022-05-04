from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
)
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes

from django.http import Http404

from products.models import Product
from .serializers import ProductSerializer

# Create your views here.

@permission_classes((AllowAny, ))
class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

@permission_classes((AllowAny, ))
class ProductDetail(RetrieveAPIView):
    serializer_class = ProductSerializer
    lookup_field = 'id'
    def get_object(self):
        id_ = self.kwargs.get('id')
        product_qs = Product.objects.filter(id=id_)
        if not product_qs.exists():
            raise Http404
        return product_qs.first()