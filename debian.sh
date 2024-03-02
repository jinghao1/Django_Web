#!/bin/bash
apt-get update
apt-get install python3 python3-pip git python3-venv
cd /home/Django_Web

.env/Dj_web/bin/python3 -m pip install --upgrade pip
.env/Dj_web/bin/python3 -m pip install package_name
source .env/Dj_web/bin/activate
apt-get install libmariadb-dev-compat libmariadb-dev libjpeg-dev
pip3 install -r requirements.txt
#https://blog.csdn.net/2202_75762088/article/details/134625775
##python version 3.6.15
# install  docker
# https://blog.csdn.net/qq_43329216/article/details/134543375