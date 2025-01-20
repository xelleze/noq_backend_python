from .common import *
import os

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = False

SERVER_IPS = os.environ.get('ALLOWED_HOSTS',"").split(",")

ALLOWED_HOSTS = ["127.0.0.1", "localhost", ] + SERVER_IPS

CORS_ALLOWED_ORIGINS = [ 
    f'http://{ip}' for ip in SERVER_IPS 
]

CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^http:\/\/localhost:*([0-9]+)?$",
]

# För att säkerställa att session- och CSRF-cookies används för alla subdomäner under .noqapp.se
SESSION_COOKIE_DOMAIN = '.noqapp.se'
CSRF_COOKIE_DOMAIN = '.noqapp.se'

# Django Cookie Secure Settings
SESSION_COOKIE_SECURE = False  # Använd True för https
CSRF_COOKIE_SECURE = False  # Använd True för https

SESSION_COOKIE_SAMESITE = 'None'  # Tillåt att session-cookies skickas över subdomäner
CSRF_COOKIE_SAMESITE = 'None'    # Tillåt att CSRF-cookies skickas över subdomäner


CORS_ALLOW_CREDENTIALS = True


SECURE_CROSS_ORIGIN_OPENER_POLICY = None

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ.get('DB_HOST'),
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASS'),
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/static/'
MEDIA_URL = '/static/media/'

MEDIA_ROOT = '/vol/web/media'
STATIC_ROOT = '/vol/web/static'
