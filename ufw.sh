#!/usr/bin/bash

sudo ufw allow 22/tcp
sudo ufw allow 443/tcp
sudo ufw allow 80/tcp
sudo ufw status
sudo ufw enable
sudo ufw status
