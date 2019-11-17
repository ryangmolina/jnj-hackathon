#!/bin/bash

RUN_DIR='/srv/oscar/project/run'
LOG_DIR='/srv/oscar/project/logs'
LOG_LEVEL='INFO'

echo 'Starting worker(s)'
celery -A config multi start w1 \
  --loglevel=$LOG_LEVEL \
  --logfile=$LOG_DIR/%n.log \
  --pidfile=$RUN_DIR/%n.pid
