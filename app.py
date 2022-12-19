import os
import sys
import pathlib

BASE_DIR = pathlib.Path(__file__).resolve().parent

PATHS = [
    str(BASE_DIR / "apps"),
    str(BASE_DIR / "apps" / "web"),
    str(BASE_DIR / "apps" / "web" / "backend"),
]

sys.path.extend(PATHS)

os.environ["DJANGO_SETTINGS_MODULE"] = "settings"
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

import django
django.setup()

from apps.web.backend import asgi
app = asgi.app