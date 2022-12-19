from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import (
    include,
    path,
    re_path,
)

from pages.views import error_404
from checkout.views import (
    checkout_view, 
    checkout_success_view,
)

djangoAdminUrlPatterns = [
    path('admin/', admin.site.urls),
]

djangoUrls = [
    path('accounts/', include('accounts.urls')),
    re_path(r"^checkout/$", checkout_view, name='checkout'),
    re_path(r"^checkout-success/$", checkout_success_view, name='checkout-success'),
    re_path(r"^error/$", error_404, name='404'),
]

djangoApiUrlPatterns = [
    path('api/products/', include('products.api.urls')),
    path('api/category/', include('category.api.urls')),
    path('api/cart/', include('carts.api.urls')),
    # path('api/search/', include('search.urls')),
]

localUrlPatterns = []

if settings.DEBUG:
    localUrlPatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    localUrlPatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)