#!/bin/bash

cp scripts/conf/gunicorn.conf /etc/supervisor/conf.d/
. /srv/oscar/env/venv/bin/activate
supervisorctl restart gunicorn
deactivate
