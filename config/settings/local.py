from .base import *
import json
import os

# secret.json 로드
with open(os.path.join(BASE_DIR, 'secret.json')) as f:
    SECRET = json.load(f)

DEBUG = True

ALLOWED_HOSTS = []

# Static & Media
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / '.static_root'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

# MySQL 연동
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': SECRET['DB']['NAME'],
        'USER': SECRET['DB']['USER'],
        'PASSWORD': SECRET['DB']['PASSWORD'],
        'HOST': SECRET['DB']['HOST'],
        'PORT': SECRET['DB']['PORT'],
    }
}
