from re import T
from decouple import config

from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hf6*cde(@0vf-t!7)jvt6swwi69%@&ma0a4_!oiv4$lx_ri0y%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DJANGO_DEBUG', cast=bool, default=1)

ALLOWED_HOSTS = ['*']

CORS_ALLOW_ALL_ORIGINS: bool = True

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

STATICFILES_DIRS = [
    BASE_DIR.parent / 'public'
]

STATIC_ROOT = BASE_DIR.parent.parent / 'staticfiles_build' / 'static'

LOGIN_URL = 'sign-in'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = config('DJANGO_EMAIL_USER', cast=str)
EMAIL_HOST_PASSWORD = config('DJANGO_EMAIL_PASSWORD', cast=str)
EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

INTERNAL_IPS = (
    '127.0.0.1',
    '192.168.1.23',
    'localhost:3000',
)

APPEND_SLASH = True