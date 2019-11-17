#!/bin/bash
# Folders should be 755 files should be 644

OWNER=$1
GROUP=$2

echo "--> Cleaning artifacts"
cd /srv/oscar/project && make clean

cd /srv/oscar/project
echo "--> Normalizing permissions and ownership on the app folder"
chown $OWNER:$GROUP -Rf app
chmod 755 app
find app -type "d" | xargs chmod 755
find app -type "f" | xargs chmod 644
chmod +x app/manage.py

echo "--> Normalizing permissions and ownership on the assets and static folders"
find app/assets/ -type "f" | xargs chmod 755
find app/static/ -type "f" | xargs chmod 755

echo "--> Normalizing permissions and ownership on the logs folder"
chown $OWNER:$GROUP -Rf logs
chmod 755 logs
find logs -type "d" | xargs chmod 755
find logs -type "f" | xargs chmod 644

echo "--> Normalizing permissions and ownership on the db folder"
chown $OWNER:$GROUP -f db
chmod 755 db

echo "--> Normalizing permissions and ownership on the run folder"
chown $OWNER:$GROUP -f run
chmod 755 run
