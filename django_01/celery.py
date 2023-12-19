import os
import django
from celery import Celery
from django.conf import settings
from celery.schedules import crontab
# 设置系统环境变量，安装django，必须设置，否则在启动celery时会报错
# celery_study 是当前项目名
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_01.settings')
# django.setup()

celery_app = Celery('taskApp')
celery_app.config_from_object('django.conf:settings')
celery_app.autodiscover_tasks(settings.INSTALLED_APPS)