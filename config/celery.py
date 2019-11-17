import os

from celery import Celery

from django.conf import settings

app_env = os.environ.get('APP_ENV', 'prod')
os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'config.settings.{}'.format(app_env)
)

app = Celery('config')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
