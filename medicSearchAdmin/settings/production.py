from .settings import *

DEBUG = True

SECRET_KEY = '6$k1vn&-+u!64&y^c+ze)2&vo!w+p_!qu2lgg3%2@*9^6w=kq@'

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
