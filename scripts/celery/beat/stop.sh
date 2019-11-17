#!/bin/bash

cp scripts/conf/celerybeat.conf /etc/supervisor/conf.d/
. /srv/oscar/env/venv/bin/activate
supervisorctl stop celerybeat
deactivate
