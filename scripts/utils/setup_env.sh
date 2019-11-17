#!/bin/bash

# Clean any artifacts
echo "--> Cleaning artifacts"
cd /srv/oscar/project && make clean


# Make sure that the docker container can write to these directories
echo "--> Updating permissions for docker access"
find /srv/oscar/project -iname "migrations" -type "d" | xargs chmod 777
chmod 777 /srv/oscar/project/run
chmod 777 /srv/oscar/project/logs
chmod 777 /srv/oscar/project/logs/*.log
chmod 777 /srv/oscar/project/db
chmod 777 /srv/oscar/project/app/static


# Build the approriate environment
echo "--> Building the environment"
make deploy


# Apply migrations
echo "--> Applying migrations"
cd /srv/oscar/project
source scripts/utils/django_manage.sh migrate
