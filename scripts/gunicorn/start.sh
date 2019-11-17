#!/bin/bash

cp scripts/conf/gunicorn.conf /etc/supervisor/conf.d/
. /srv/oscar/env/venv/bin/activate
supervisorctl reread
supervisorctl update
supervisorctl restart gunicorn
deactivate
