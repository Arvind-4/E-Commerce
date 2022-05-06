import os

from dotenv import load_dotenv

from .base import *

load_dotenv()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hf6*cde(@0vf-t!7)jvt6swwi69%@&ma0a4_!oiv4$lx_ri0y%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://127.0.0.1:3000',
]

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
    BASE_DIR / 'static-dev'
]
STATIC_ROOT = BASE_DIR / 'static'

LOGIN_URL = 'sign-in'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD')
EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ALGOLIA_APPLICATION_ID = str(os.environ.get('ALGOLIA_APPLICATION_ID'))
ALGOLIA_API_KEY = str(os.environ.get('ALGOLIA_API_KEY'))

ALGOLIA = {
    'APPLICATION_ID': ALGOLIA_APPLICATION_ID,
    'API_KEY': ALGOLIA_API_KEY
}

INTERNAL_IPS = (
    '127.0.0.1',
    '192.168.1.23',
    'localhost:3000',
)