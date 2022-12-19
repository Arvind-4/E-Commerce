import os

os.environ["DJANGO_SETTINGS_MODULE"] = 'backend.settings'
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

import django
django.setup()

from django.core.asgi import get_asgi_application

app = get_asgi_application()
