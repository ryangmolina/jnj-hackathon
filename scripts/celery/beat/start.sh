#!/bin/bash

cp scripts/conf/celerybeat.conf /etc/supervisor/conf.d/
. /srv/oscar/env/venv/bin/activate
supervisorctl reread
supervisorctl update
supervisorctl restart celerybeat
deactivate
