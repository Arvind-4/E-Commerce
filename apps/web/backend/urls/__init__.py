from .django_urls import (
    djangoAdminUrlPatterns,
    djangoUrls,
    djangoApiUrlPatterns,
    localUrlPatterns,
)
from .react_urls import reactUrls

urlpatterns = djangoAdminUrlPatterns + djangoUrls + djangoApiUrlPatterns + reactUrls + localUrlPatterns