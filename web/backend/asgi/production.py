import os

settingsModule = 'backend.settings'

os.environ["DJANGO_SETTINGS_MODULE"] = settingsModule
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

import django

django.setup()

from django.core.asgi import get_asgi_application

from backend.django_algolia.client import initialize_algolia

application = get_asgi_application()

initialize_algolia()