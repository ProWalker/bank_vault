import os
import dj_database_url

from dotenv import load_dotenv
from distutils.util import strtobool
load_dotenv()

db_engine = 'django.db.backends.postgresql_psycopg2'

DATABASES = {
    'default': dj_database_url.parse(os.getenv('DB_URL'), db_engine)
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = strtobool(os.getenv('DEBUG'))

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = ['*']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
