#!/bin/bash

echo "Installing and setting up supervisord"
source /srv/oscar/project/scripts/supervisord/setup_supervisord.sh
echo "--> [all] Setting up environment"
source /srv/oscar/project/scripts/utils/set_env_var.sh APP_ENV $APP_ENV
source /srv/oscar/project/scripts/utils/setup_env.sh

# Run the app
/usr/sbin/sshd -D
