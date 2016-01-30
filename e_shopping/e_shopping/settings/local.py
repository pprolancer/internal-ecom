from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'internal-ecom',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'USER': 'cis',
        'PASSWORD': '123'
    }
}