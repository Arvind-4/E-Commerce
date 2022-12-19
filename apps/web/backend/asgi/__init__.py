try:
    from .production import * # noqa
except Exception as e:
    print(str(e))
    from .dev import *  # noqa