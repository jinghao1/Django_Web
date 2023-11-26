FROM python:3.6
WORKDIR /app
COPY . /app
RUN apt update
RUN apt install make

RUN pip install -r requirements.txt
#RUN python manage.py make migrations
#RUN python manage.py migrate
