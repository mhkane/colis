"""
Django settings for airspress project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from authomatic.providers import oauth2, oauth1, openid
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'spb_fb$xf-vyc&*^n_^ur2#mgjk32!#+3cmvs&0mr70h!=_0@2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

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
    'signup',
    'trips',
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
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

# PARSE APPLICATION KEYS
APPLICATION_ID = "#6"
REST_API_KEY = "a######################################"
MASTER_KEY = "w#########################"
#FACEBOOK login CONFIG
CONFIG = {
          
    'fb': {
           
        'class_': oauth2.Facebook,
        'id':1,
        # Facebook is an AuthorizationProvider too.
        'consumer_key': '1###############',
        'consumer_secret': '5##########################',
        'redirect_uri':'http://www.falconfake.com:8000/signup/',
        # But it is also an OAuth 2.0 provider and it needs scope.
        'scope': ['user_about_me', 'email', 'publish_stream'],
    },
    
    'oi': {
           
        # OpenID provider dependent on the python-openid package.
        'class_': openid.OpenID,
        'id':2,
    }
}
