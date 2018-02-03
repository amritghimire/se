from .base import *

DEBUG = False


DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
       'NAME': 'ci',
       'USER': 'postgres',
       'PASSWORD': 'postgres',
       'HOST': 'postgres',
       'PORT': '5432',
   },
}