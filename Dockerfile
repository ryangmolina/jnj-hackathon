FROM ubuntu:16.04

RUN mkdir -p /_build/
WORKDIR /_build/
ADD . /_build/

# Install packages and build the environment
# NOTE:
# - A non-priv user named `oscar` will be created with home dir at `/srv/oscar`
# - tmux trigger is `CTRL+t`
RUN apt-get update && apt-get install -y \
       sudo \
       build-essential \
       python3-dev \
       python3-pip \
       python-dev \
       python-pip \
       openssh-server \
       libpq-dev \
       htop \
    && pip3 install -U pip \
    && make init_env \
    && chown oscar: -R /srv/oscar \
    && mkdir /var/run/sshd

RUN pip3 install psycopg2-binary
# Clean up
RUN apt-get autoclean \
    && apt-get autoremove \
    && apt-get purge \
    && rm -Rf /_build/
