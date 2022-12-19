import os
import sys
import pathlib
from decouple import config

DJANGO_PROJECT = config("DJANGO_PROJECT", cast=str, default="")
PROJECT_DIR_PATH = pathlib.Path(__file__).resolve(strict=True).parent.parent.parent
PROJECT_DIR = PROJECT_DIR_PATH / "apps" / "web"

def init_django(project_name=None):
    project_name = project_name or DJANGO_PROJECT or "backend"
    print("project_name", project_name)
    if project_name == None:
        raise Exception("No project name provided")
    
    sys.path.insert(0, str(PROJECT_DIR))
    
    os.environ['DJANGO_SETTINGS_MODULE'] = f"{project_name}.settings"
    os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
    import django
    django.setup()
