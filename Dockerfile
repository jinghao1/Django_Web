FROM python:3.6
#FROM ubuntu:22.04
WORKDIR /app
COPY . /app
#RUN sed -i "s@http://deb.debian.org@https://mirrors.163.com@g" /etc/apt/sources.list
#RUN sed -i 's/security-cdn.debian.org/mirrors.aliyun.com' /etc/apt/sources.list


#RUN apt update
#RUN apt install make
#RUN apt install -y python3 python3-pip
#RUN apt install -y python3-dev default-libmysqlclient-dev build-essential
#RUN pip3 install --upgrade setuptools
RUN pip install -r requirements.txt
#RUN python manage.py make migrations
#RUN python manage.py migrate
RUN python3 manage.py runserver 0.0.0.0:80