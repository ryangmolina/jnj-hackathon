#!/bin/bash
# Sets environment variables system wide
#
# :param ENV_VAR: Environment variable name
# :param ENV_VAL: Environment variable value
#
ENV_VAR=APP_ENV
ENV_VAL=${APP_ENV}

ENV_FILE=/etc/environment

echo "--> [root] Setting env $ENV_VAR"
export REP_STR=$(grep $ENV_VAR $ENV_FILE)
if grep $ENV_VAR $ENV_FILE; then
    sed -i -e "s/\$REP_STR/$ENV_VAR=$ENV_VAL/g" $ENV_FILE
else
    echo $ENV_VAR=$ENV_VAL | tee -a $ENV_FILE
fi

echo "--> New environment vars"
cat $ENV_FILE
