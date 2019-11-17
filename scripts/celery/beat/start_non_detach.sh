#!/bin/bash

# Run by supervisord with oscar user
CELERY_APP='config'
CELERYBEAT_PID_FILE='/srv/oscar/project/run/beat.pid'
CELERYBEAT_LOG_FILE='/srv/oscar/project/logs/beat.log'
CELERYBEAT_LOG_LEVEL='INFO'
CELERYBEAT_SCHEDULER='django_celery_beat.schedulers:DatabaseScheduler'

exec celery -A $CELERY_APP beat -S $CELERYBEAT_SCHEDULER --pidfile $CELERYBEAT_PID_FILE -f $CELERYBEAT_LOG_FILE -l $CELERYBEAT_LOG_LEVEL
