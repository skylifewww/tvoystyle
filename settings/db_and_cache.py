import os
import dj_database_url
from django.conf.global_settings import DATABASES
# import urlparse


ATOMIC_REQUESTS = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tvoy_style',
        'USER': 'skylife',
        'PASSWORD': 'skywww123',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}

db_config = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_config)
if db_config:
    DATABASES['default'] =  db_config

# redis_url = urlparse.urlparse(os.environ.get('REDIS_URL'))
# CACHES = {
#     "default": {
#          "BACKEND": "redis_cache.RedisCache",
#          "LOCATION": "{0}:{1}".format(redis_url.hostname, redis_url.port),
#          "OPTIONS": {
#              "PASSWORD": redis_url.password,
#              "DB": 0,
#          }
#     }
# }

# CACHES = {
#     'default': {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         'LOCATION': 'redis://127.0.0.1:6379/0',
#     },
#     'local': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#         'LOCATION': 'iosDevCourse'
#     }
# }


