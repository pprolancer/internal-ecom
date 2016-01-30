from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'internal-ecom',
        'HOST': '',
        'PORT': '5432',
        'USER': '',
        'PASSWORD': ''
    }
}