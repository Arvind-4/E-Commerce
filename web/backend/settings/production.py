import os
import pathlib
from dotenv import load_dotenv

from .base import *

# SECRET_KEY: 
# ADMIN_URL: 
# DEBUG:
# ALLOWED_HOST: *.herokuapp.com
# EMAIL_USER: 
# EMAIL_PASSWORD: 

if not 'HEROKU' in os.environ:
    load_dotenv()

# Basic Settings

SECRET_KEY = str(os.environ.get('SECRET_KEY'))
ADMIN_URL = str(os.environ.get('ADMIN_URL'))
DEBUG = int(os.environ.get('DEBUG', 0))
ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOST'), 'localhost', '127.0.0.1']
CORS_ALLOWED_ORIGINS = [
    str(os.environ.get('ALLOWED_HOST'))
]

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

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD')
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

# Database Settings

NEW_BASE_DIR = pathlib.Path(BASE_DIR)

CERTIFICATE_DIR = NEW_BASE_DIR.parent

CERTIFICATE_FILE_PATH = CERTIFICATE_DIR / 'certificate' / 'root.crt'

DATABASES = {
    'default': {
        'ENGINE': 'django_cockroachdb',
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'PORT': int(os.environ.get('DATABASE_PORT')),
        'OPTIONS': {
            'sslmode': 'verify-full',
            'sslrootcert': str(CERTIFICATE_FILE_PATH),
        },
    },
}

DATABASES['default']['CONN_MAX_AGE'] = 500
DATABASES['default']['ATOMIC_REQUESTS'] = True 