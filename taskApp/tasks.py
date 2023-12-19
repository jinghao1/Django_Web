import logging
import json
import datetime
import time
import os.path
import re
# import pysftp
from celery import shared_task
# from log.log_files import Logger
from django_01.celery import celery_app
# from apps.task import ali_monitor, weather_monitor, power_monitor, over_view_monitor

# log = Logger('../log/files/data.log', level='debug')
# logger = log.logger


# @shared_task
@celery_app.task
def get_ali_script_status():
    print("ali_monitor.get_ali_status()")


@celery_app.task
def get_weather_status():
    print("weather_monitor.get_weather_status()")


@celery_app.task
def get_power_status():
    print("power_monitor")
    # power_monitor.get_power_status()

@celery_app.task
def get_overview_status():
    print("over_view_monitor")
    # over_view_monitor.get_overview_status()

@shared_task
def produce_log():
    logfile = "./task_celery.log"
    # Logger(logfile, level='debug')