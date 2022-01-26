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
from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static

from django.shortcuts import redirect, render

from pages.views import error_404

def render_main_template(request, *args, **kwargs):
    allow_block_content = ['accounts']
    context = {
        'is_authenticated': request.user.is_authenticated
    }
    return render(request, 'base.html', context)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products/', include('products.api.urls')),
    path('api/category/', include('category.api.urls')),
    path('api/cart/', include('carts.api.urls')),

    path('accounts/', include('accounts.urls')),

    path('error/', error_404, name='404'),

    re_path(r'^.*', render_main_template, name='home')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
