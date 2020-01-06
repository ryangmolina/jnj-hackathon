import os
import json

# This is the only allowed django-related package to be imported into
# our settings file.
from django.core.exceptions import ImproperlyConfigured


###### PATH CONFIGURATION
CONFIG_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SETTINGS_DIR = os.path.join(CONFIG_DIR, 'settings')
APP_DIR = os.path.join(os.path.dirname(CONFIG_DIR), 'app')
PROJECT_DIR = os.path.dirname(CONFIG_DIR)
RUN_DIR = os.path.join(PROJECT_DIR, 'run')
LOG_DIR = os.path.join(PROJECT_DIR, 'logs')
MEDIA_DIR = os.path.join(APP_DIR, 'media')
FRONTEND_DIR = os.path.join(PROJECT_DIR, 'frontend')
SITE_NAME = 'new'


DEBUG = True


# Application definition

AUTH_USER_MODEL = 'accounts.Account'

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'allauth.socialaccount.providers.google',

    'django_celery_beat',

    'rest_framework',
    'drf_multiple_model',

    'django_js_reverse',
    'notifications',

    'webpack_loader',
]

LOCAL_APPS = [
    'app.core',
    'app.accounts.apps.AccountsConfig',
    'app.api',
    'app.dashboard',
    'app.services',
    'app.forms',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(APP_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'config.wsgi.application'

# https://docs.djangoproject.com/en/2.0/ref/settings/#append-slash
APPEND_SLASH = True

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/assets/'
STATIC_ROOT = os.path.join(APP_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(APP_DIR, 'assets'),
]

##### MEDIA CONFIGURATION
# https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-MEDIA_ROOT
# https://docs.djangoproject.com/en/2.0/ref/settings/#media-url
MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = '/media/'

###### LOGGING CONFIGURATION
# https://docs.djangoproject.com/en/1.9/topics/logging/
LOG_FILE = os.path.join(LOG_DIR, '{}.log'.format(SITE_NAME))
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s %(name)s %(pathname)s %(lineno)d - %(message)s'
        },
        'simple': {
            'format': '[%(asctime)s] %(levelname)s %(module)s - %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_FILE,
            'maxBytes': 1024*1024*10,  # 10 megabytes
            'backupCount': 10,
            'formatter': 'verbose'
        },
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': False,
        },
        'default': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}

###### REST_FRAMEWORK CONFIGURATION
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
}

###### CELERY CONFIGURATION
BROKER_USER = 'rabbitmquser'
BROKER_PASS = 'rabbitmqpass'
BROKER_VHOST = 'rabbitmq_vhost'
BROKER_HOST = 'main_rabbitmq'
BROKER_PORT = 5672
BROKER_URL = 'amqp://{}:{}@{}:{}/{}'.format(
    BROKER_USER,
    BROKER_PASS,
    BROKER_HOST,
    BROKER_PORT,
    BROKER_VHOST
)

SITE_ID = 1

#### DJANGO ALLAUTH CONFIGURATION ####
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_USERNAME_MIN_LENGTH = 4
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True

LOGIN_REDIRECT_URL = '/account/dashboard'
# Page to redirect when user confirmed the account via email
# but no user is authenticated yet. Since we enable auto login
# after confirmation, we should redirect them to their profile
LOGIN_URL = '/account/dashboard'

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

# WEBPACK CONFIGURATION
WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': False,
        'BUNDLE_DIR_NAME': 'webpack_bundles/',  # must end with slash
        'STATS_FILE': os.path.join(FRONTEND_DIR, 'webpack-stats.json'),
        'POLL_INTERVAL': 0.1,
        'TIMEOUT': None,
        'IGNORE': ['.+\.hot-update.js', '.+\.map']
    }
}



# Sendgrid Settings
SENDGRID_API_KEY = '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'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'Team Ubuntu <info@teamubuntu.com>'
