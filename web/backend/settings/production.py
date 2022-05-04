import os
import pathlib
from dotenv import load_dotenv

from .base import *

if not 'HEROKU' in os.environ:
    load_dotenv()

# Basic Settings

SECRET_KEY = str(os.environ.get('DJANGO_SECRET_KEY'))

ADMIN_URL = str(os.environ.get('DJANGO_ADMIN_URL'))

DEBUG = bool(int(os.environ.get('DJANGO_DEBUG')))

ALLOWED_HOSTS = []

ALLOWED_HOSTS.extend(
    filter(
        None,
        os.environ.get('DJANGO_ALLOWED_HOSTS').split(','),
    )
)

CORS_ALLOWED_ORIGINS = [] # str(os.environ.get('DJANGO_CORS_ALLOWED_ORIGINS'))

CORS_ALLOWED_ORIGINS.extend(
    filter(
        None,
        os.environ.get('DJANGO_CORS_ALLOWED_ORIGINS').split(','),
    )
)

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
    BASE_DIR / 'static-dev'
]
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Security Settings

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

# Algolia Settings

ALGOLIA_APPLICATION_ID = str(os.environ.get('ALGOLIA_APPLICATION_ID'))
ALGOLIA_API_KEY = str(os.environ.get('ALGOLIA_API_KEY'))

ALGOLIA = {
    'APPLICATION_ID': ALGOLIA_APPLICATION_ID,
    'API_KEY': ALGOLIA_API_KEY
}

# Database Settings

DATABASE_NAME = str(os.environ.get('DATABASE_NAME'))
DATABASE_USER = str(os.environ.get('DATABASE_USER'))
DATABASE_PASSWORD = str(os.environ.get('DATABASE_PASSWORD'))
DATABASE_HOST = str(os.environ.get('DATABASE_HOST'))
DATABASE_PORT = str(os.environ.get('DATABASE_PORT'))

NEW_BASE_DIR = pathlib.Path(BASE_DIR)

CERTIFICATE_DIR = NEW_BASE_DIR.parent

CERTIFICATE_FILE_PATH = CERTIFICATE_DIR / 'certificate' / 'root.crt'

DB_IS_AVAILABLE = all([
    DATABASE_NAME,
    DATABASE_USER,
    DATABASE_PASSWORD,
    DATABASE_HOST,
    DATABASE_PORT,
    CERTIFICATE_FILE_PATH
])

if DB_IS_AVAILABLE:
    DATABASES = {
        'default': {
            'ENGINE': 'django_cockroachdb',
            'NAME': DATABASE_NAME,
            'USER': DATABASE_USER,
            'PASSWORD': DATABASE_PASSWORD,
            'HOST': DATABASE_HOST,
            'PORT': DATABASE_PORT,
            'OPTIONS': {
                'sslmode': 'verify-full',
                'sslrootcert': str(CERTIFICATE_FILE_PATH),
            },
        },
    }

    DATABASES['default']['CONN_MAX_AGE'] = 500
    DATABASES['default']['ATOMIC_REQUESTS'] = True 