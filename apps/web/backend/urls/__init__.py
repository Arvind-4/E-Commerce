from .django_urls import (
    djangoAdminUrlPatterns,
    djangoUrls,
    djangoApiUrlPatterns,
    localUrlPatterns,
)
from .react_urls import reactUrls

urlpatterns = djangoAdminUrlPatterns + djangoUrls + djangoApiUrlPatterns + reactUrls + localUrlPatterns

handler404 = 'pages.views.handler404'
handler500 = 'pages.views.handler500'