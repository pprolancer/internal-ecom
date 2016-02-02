from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'internalecom',
        'HOST': 'localhost',
        'PORT': '5432',
        'USER': 'chills',
        'PASSWORD': 'raWoDwigaKaUYW'
    }
}