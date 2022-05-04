"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import (
    path, 
    include, 
    re_path,
)
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


from pages.views import error_404
from checkout.views import (
    checkout_view, 
    checkout_success_view,
)

djangoUrlPatterns = [
    path('admin/', admin.site.urls),
]

apiUrlPatterns = [
    path('api/products/', include('products.api.urls')),
    path('api/category/', include('category.api.urls')),
    path('api/cart/', include('carts.api.urls')),
    path('api/search/', include('search.urls')),
]

defaultUrlPatterns = [
    path('accounts/', include('accounts.urls')),
    path('checkout/', checkout_view, name='checkout'),
    path('checkout-success/', checkout_success_view, name='checkout-success'),

    path('error/', error_404, name='404'),
]

reactUrlPatterns = [
    re_path(r'^.*', TemplateView.as_view(template_name='base.html'), name='home')
]

localUrlPatterns = []

if settings.DEBUG:
    localUrlPatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    localUrlPatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = djangoUrlPatterns + apiUrlPatterns + defaultUrlPatterns + reactUrlPatterns + localUrlPatterns