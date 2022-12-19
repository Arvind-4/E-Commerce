import os
import pathlib
from decouple import (
    config,
    Csv
)

from .base import *    

# Basic Settings

SECRET_KEY = config('DJANGO_SECRET_KEY', cast=str)

ADMIN_URL = config('DJANGO_ADMIN_URL', cast=str)

DEBUG = config('DJANGO_DEBUG', cast=bool)

HOSTS = config('DJANGO_ALLOWED_HOSTS', cast=str)
ALLOWED_HOSTS = HOSTS.split(",")

CORS_ORIGIN = config('DJANGO_CORS_ALLOWED_ORIGINS', cast=str)
CORS_ALLOWED_ORIGINS = CORS_ORIGIN.split(",")

# Authentication Settings

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
}

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)
AUTH_USER_MODEL = 'accounts.Account'
LOGIN_URL = 'sign-in'

# Email Settings

EMAIL_USER = str(os.environ.get('EMAIL_USER'))
EMAIL_PASSWORD = str(os.environ.get('EMAIL_PASSWORD'))

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = EMAIL_USER
EMAIL_HOST_PASSWORD = EMAIL_PASSWORD
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Static Settings

STATICFILES_DIRS = [
    BASE_DIR.parent / 'public'
]

STATIC_ROOT = BASE_DIR.parent.parent / 'staticfiles_build' / 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

APPEND_SLASH = True

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Security Settings

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

# Database Settings

from backend.db.postgres_db import * #noqa