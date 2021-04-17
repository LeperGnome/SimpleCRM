from .base import *


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_name',
        'USER': 'user_name',
        'PASSWORD': 'user_pass',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'verysecret'
