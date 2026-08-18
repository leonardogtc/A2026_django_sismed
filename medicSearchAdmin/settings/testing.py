from .settings import *

DEBUG = True

SECRET_KEY = '$wrau&$=#0plkq17*ec5re52e*07q4y2k^8@j)o+busktkb(be'

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
