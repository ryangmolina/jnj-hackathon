#!/bin/bash

echo 'Creating virtual environment for supervisord'
pip install virtualenv
virtualenv --python=/usr/bin/python2.7 /srv/oscar/env/venv
. /srv/oscar/env/venv/bin/activate

echo 'Installing supervisord'
pip install supervisor

echo 'Moving supervisord conf'
mkdir -p /etc/supervisor/conf.d
cp /srv/oscar/project/scripts/conf/supervisord.conf /etc/supervisor/
chmod 644 /etc/supervisor/supervisord.conf
supervisord
deactivate
