"""
Django settings for airspress project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from authomatic.providers import oauth2
from django.conf.global_settings import SESSION_ENGINE
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'spb_fb$xf-vyc&*^n_^ur2#mgjk32!#+3cmvs&0mr70h!=_0@2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []
# MEDIA URL
'''
TEMPLATE_CONTEXT_PROCESSORS = (

  "django.core.context_processors.media",
)
'''
STATICFILES_FINDERS = ( 
                       'django.contrib.staticfiles.finders.FileSystemFinder',
                       'django.contrib.staticfiles.finders.AppDirectoriesFinder',
                       )
#Uploaded Files
FILE_UPLOAD_DIR = 'c:/'
# TEMPLATEs directory
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'signup',
    'trips',
    'account',
    'paypalrestsdk',
    'asp_payment',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'airspress.urls'

WSGI_APPLICATION = 'airspress.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'airspress',
        'USER': 'postgres',
        'PASSWORD': 'Shinsekai',
        'HOST': '',
        'PORT':'5432',
    }
}

SOUTH_DATABASE_ADAPTERS = {
  'default': 'south.db.postgresql_psycopg2'
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
DATE_INPUT_FORMATS = ['%m-%d-%Y','%d-%m-%Y','%Y-%m-%d',
                      ]
# mEDIA FILES User-uploaded ones
MEDIA_URL = '/media/'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
#Paypal Credentials
PAYPAL_MODE='sandbox' #or 'live'
PAYPAL_ID = 'AasK0xBGMLG8RARnY-SwXrdw_hCADnC2qCYjoPaNHDWIJSrcPvF0J10eyT4t'
PAYPAL_SECRET ='EJqwBRDBF932t3jOO--kd23etAlxcFS-3Tys717xJkW7s1CPdU34ThvQo4bv'
# PARSE APPLICATION KEYS
APPLICATION_ID = "9GC4ybpn3PxuHyfCm3JKQZXyC1WBNuiTzhRcTHo6"
REST_API_KEY = "asSPhJ5AV70NOyohcnRWLqXWtL5OrVNZV68yq6Tu"
MASTER_KEY = "wzDarFuVlJHUI9vPEKZwfKVnluLYBRazv6KT1fKP"
#FACEBOOK login CONFIG
consumer_secret = '5f199d47d0bd5ea9f7f9a6c379a4d139'
consumer_key = '1537229933223161'
CONFIG = {
          
    'fb': {
           
        'class_': oauth2.Facebook,
        'id':1,
        # Facebook is an AuthorizationProvider too.
        'consumer_key': consumer_key,
        'consumer_secret': consumer_secret ,
        # But it is also an OAuth 2.0 provider and it needs scope.
        'scope': ['user_about_me', 'email', 'publish_stream'],
    },
    
}

#SESSIONS Settings
SESSION_ENGINE = "django.contrib.sessions.backends.db"
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_AGE = 1800
#SESSION_COOKIE_SECURE = True #Only on Production