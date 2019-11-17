#!/bin/bash

ACTION=$1
if [[ $ACTION == 'collectstatic_js_reverse' ]]; then
    sudo su - oscar -c """
    cd /srv/oscar/project
    python3 manage.py $ACTION --settings=config.settings.\$APP_ENV
    """
elif [[ $ACTION == collectstatic* ]]; then
    sudo su - oscar -c """
    cd /srv/oscar/project
    python3 manage.py $ACTION --no-input --settings=config.settings.\$APP_ENV
    """
elif [[ $ACTION == runserver* ]]; then
    sudo su - oscar -c """
    cd /srv/oscar/project
    python3 manage.py $ACTION 0.0.0.0:8000 --settings=config.settings.\$APP_ENV
    """
else
    sudo su - oscar -c """
    cd /srv/oscar/project
    python3 manage.py $ACTION --settings=config.settings.\$APP_ENV
    """
fi
