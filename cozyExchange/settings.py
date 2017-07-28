"""
Django settings for cozyExchange project.
Generated by 'django-admin startproject' using Django 1.10.6.
For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'hello@cozy.nyc'
EMAIL_HOST_PASSWORD = 'pasword'
EMAIL_PORT = '587'
EMAIL_USE_TLS = True

# Quick-start development settings - unsuitable for production[-]
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5e8$r+s03xq=&p^@nw7v6f=p3nv)4j)9gmqha=xh%2o$x2bcq+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'profiles',
    'contact',
    'shop',
    'cuser',
    'rest_framework',
]

POSTMAN_AUTO_MODERATE_AS = True
POSTMAN_DISALLOW_ANONYMOUS = True
POSTMAN_DISALLOW_MULTIRECIPIENTS = True
POSTMAN_DISABLE_USER_EMAILING = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cozyExchange.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    )

WSGI_APPLICATION = 'cozyExchange.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

if DEBUG:
    MEDIA_URL = '/media/'
    STATIC_ROOT = os.path.join(BASE_DIR, "static", "static-only")
    MEDIA_ROOT = os.path.join(BASE_DIR, "static", "media")
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, "static", "static"),
    )

SITE_ID = 1

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'

AUTH_USER_MODEL = 'cuser.User'

# ACCOUNT_AUTHENTICATION_METHOD = "username_email"
# ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = LOGIN_URL
# ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = None
# ACCOUNT_CONFIRM_EMAIL_ON_GET = False
#
# ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 5
# ACCOUNT_EMAIL_REQUIRED = False
# ACCOUNT_EMAIL_VERIFICATION = None
# ACCOUNT_EMAIL_SUBJECT_PREFIX = "Insert Subject"
#
# ACCOUNT_LOGOUT_ON_GET = True
# ACCOUNT_LOGOUT_REDIRECT_URL = '/'
# ACCOUNT_SIGNUP_FORM_CLASS = None
# ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = True
# ACCOUNT_UNIQUE_EMAIL = True
# ACCOUNT_USER_MODEL_USERNAME_FIELD = "username"
# ACCOUNT_USER_MODEL_EMAIL_FIELD = "email"
#
# ACCOUNT_USERNAME_MIN_LENGTH  = 1
# ACCOUNT_USERNAME_BLACKLIST = []
# ACCOUNT_USERNAME_REQUIRED = True
# ACCOUNT_PASSWORD_INPUT_RENDER_VALUE = False
# ACCOUNT_PASSWORD_MIN_LENGTH = 6
# ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True


#stripe
#Test
# STRIPE_PUBLISHBLE_KEY = 'pk_test_FdNbuY3HOw6hMkBA9uHh4A1m'
# STRIPE_SECERT_KEY = 'sk_test_j72JVcWLX4XSKZY8lzdtcJHt'

#Live
# STRIPE_PUBLISHBLE_KEY = 'pk_live_MiY76HJdhaCXjokwKyfTy9yO'
# STRIPE_SECERT_KEY = 'sk_live_HtmlR1UFZYm5NikZflqKyog5'
