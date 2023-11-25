FROM python:3.7-alpine
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
RUN python manage.py make migrations
RUN python manage.py migrate
