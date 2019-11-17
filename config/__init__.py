# This ensures that celery app is imported when Django starts so that the
# `shared_task` decorator can use it.
from .celery import app as celery_app
