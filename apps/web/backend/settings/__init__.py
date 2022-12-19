from decouple import config

DJANGO_LIVE = config("DJANGO_LIVE", cast=bool, default=False)
if DJANGO_LIVE:
    print("Production Settings")
    from .production import *
else:
    print("Local Settings")    
    from .local import *
