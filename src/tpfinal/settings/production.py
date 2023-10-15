from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']


# escribime la configuracion de la base de datos sqlite

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'BlogDb',
#         'USER': 'postgres_user',
#         'PASSWORD': 'postgres_pass',
#         'HOST': 'db',
#         'PORT': '5432',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}
