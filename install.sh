#!/bin/bash

if [[ $(/usr/bin/id -u) -ne 0 ]]; then
    echo "Bitte starte dieses Skript mit root-Rechten neu."
    exit
fi

apt update

# Python und dependencies

apt install -y python3-pip
pip3 install selenium
pip3 install requests

# Google Chrome

curl -LO https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt install -y ./google-chrome-stable_current_amd64.deb
rm google-chrome-stable_current_amd64.deb 

# Chrome Driver

apt install -y unzip

CHROME_DRIVER_VERSION=`curl -sS https://chromedriver.storage.googleapis.com/LATEST_RELEASE`

wget -N https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip -P ~/
unzip ~/chromedriver_linux64.zip -d ~/
rm ~/chromedriver_linux64.zip
mv -f ~/chromedriver /usr/bin/chromedriver
chown root:root /usr/bin/chromedriver
chmod 0755 /usr/bin/chromedriver