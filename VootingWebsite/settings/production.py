from .base import *
import psycopg2
import dj_database_url

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k_(vx7o4b5n68l%a#=bongh)bs+64$$4vlyn@6xj@mz7=#m&=@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', ]

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

if 'DATABASE_URL' in os.environ:
    DATABASES = {'default': dj_database_url.config()}

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.getenv('EMAIL')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_PASSWORD')
