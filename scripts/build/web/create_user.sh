#!/bin/bash
EDGEPI_APP_USER=oscar
EDGEPI_APP_HOME=/srv/oscar
EDGEPI_SUDO_USER=edge
EDGEPI_SUDO_PASS=happy@1234


echo "--> Creating superuser '$EDGEPI_SUDO_USER'"
sudo useradd --user-group --no-create-home \
    --shell /bin/bash \
    $EDGEPI_SUDO_USER
echo $EDGEPI_SUDO_USER:$EDGEPI_SUDO_PASS | sudo chpasswd
sudo adduser $EDGEPI_SUDO_USER sudo
echo "$EDGEPI_SUDO_USER ALL=(ALL) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/90-cloud-init-users

echo "--> Creating application user '$EDGEPI_APP_USER'"
sudo mkdir -p $EDGEPI_APP_HOME
sudo useradd --system --user-group \
    --shell /bin/bash \
    --home-dir $EDGEPI_APP_HOME \
    $EDGEPI_APP_USER
sudo chown $EDGEPI_APP_USER: $EDGEPI_APP_HOME

echo "--> Updating user '$EDGEPI_SUDO_USER' and '$EDGEPI_APP_USER' groups"
sudo usermod -aG $EDGEPI_APP_USER $EDGEPI_SUDO_USER
sudo usermod -aG $EDGEPI_SUDO_USER $EDGEPI_APP_USER
