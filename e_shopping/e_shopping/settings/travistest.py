from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

SECRET_KEY = 'super_secret_key'

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'e_shopping/db.sqlite3'),
    }
}
