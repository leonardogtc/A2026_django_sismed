from medicSearchAdmin.settings.settings import SECRET_KEY

from .settings import *

DEBUG = True

SECRET_KEY = 'n@k%c*yz+1w7_87!20h+)rjdpn(*n3xx52g1#bi!g6o-1e36*0'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
