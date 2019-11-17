from .base import *

DEBUG = True

ALLOWED_HOSTS = [
    '*'
]

SECRET_KEY = os.getenv('SECRET_KEY'),

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': 'dev-postgres',
        'PORT': 5432,
    }
}

# Celery Config
BROKER_USER = os.getenv('RABBITMQ_DEFAULT_USER')
BROKER_PASS = os.getenv('RABBITMQ_DEFAULT_PASS')
BROKER_VHOST = os.getenv('RABBITMQ_DEFAULT_VHOST')
BROKER_HOST = 'dev-rq'
BROKER_PORT = 5672
BROKER_URL = 'amqp://{}:{}@{}:{}/{}'.format(
    BROKER_USER,
    BROKER_PASS,
    BROKER_HOST,
    BROKER_PORT,
    BROKER_VHOST
)
