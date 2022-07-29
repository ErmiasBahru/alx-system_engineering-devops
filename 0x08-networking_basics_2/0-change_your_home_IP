#!/usr/bin/env bash
# script that configures an Ubuntu server with the below requirements
# localhost resolves to 127.0.0.2
# facebook.com resolves to 8.8.8.8

cp /etc/hosts ~/hosts.new
sed -i s/127.0.0.1/127.0.0.2/ ~/hosts.new
echo -e "8.8.8.8\tfacebook.com" >>~/hosts.new
cp -f ~/hosts.new /etc/hosts
