#!/bin/bash
#apt-get update
cd /app
pip install -r requirements.txt
python manage.py runserver 0.0.0.0:80 &
echo "success"
while true
do
    sleep 100
    echo "endless loop"
done