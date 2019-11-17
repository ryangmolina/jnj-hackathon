#!/bin/bash

DJANGO_SETTINGS=config.settings.$APP_ENV
DJANGO_WSGI=config.wsgi
SOCKFILE=/srv/oscar/project/run/gunicorn.sock
PIDFILE=/srv/oscar/project/run/gunicorn.pid
LOG_FILE=/srv/oscar/project/logs/gunicorn.log
LOG_LEVEL=debug
NUM_WORKERS=3

# Delete any existing sock and pid files
rm -f $PIDFILE $SOCKFILE

echo "-> Starting gunicorn:edgepi as user oscar"
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS
export PYTHONPATH=/srv/oscar/project:\$PYTHONPATH
exec gunicorn \
    ${DJANGO_WSGI}:application \
    --name edgepi \
    --user oscar \
    --group oscar \
    --workers $NUM_WORKERS \
    --bind=unix:$SOCKFILE \
    --log-level=$LOG_LEVEL \
    --log-file=$LOG_FILE \
    --pid=$PIDFILE \
