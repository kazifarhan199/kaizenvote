from .base import *
import psycopg2

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k_(vx7o4b5n68l%a#=bongh)bs+64$$4vlyn@6xj@mz7=#m&=@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', ]

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'VootingWebsite',
        'USER': 'VootingWebsite',
        'PASSWORD': 'VootingWebsite',
        'HOST': '',
        'PORT': '',
    }
}

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.getenv('EMAIL')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_PASSWORD')
