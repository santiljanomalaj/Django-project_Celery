# import os
# from celery import Celery
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'abanerd_django.settings-old')
#
# app = Celery('abanerd_django')
# app.config_from_object('django.conf:settings-old', namespace='CELERY')
# app.autodiscover_tasks()


"""
Celery config file

https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html

"""
from __future__ import absolute_import
import os
from celery import Celery
from abanerd_django import settings

# this code copied from manage.py
# set the default Django settings-old module for the 'celery' app.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'abanerd_django.settings')

# you change change the name here
app = Celery("abanerd_django")

# read config from Django settings-old, the CELERY namespace would make celery
# config keys has `CELERY` prefix
app.config_from_object('django.conf:settings', namespace='CELERY')
#
# app.conf.broker_url = 'redis://localhost:6379/0'

# load tasks.py in django apps
# app.autodiscover_tasks(lambda: settings-old.INSTALLED_APPS)
app.autodiscover_tasks()


@app.task
def add(x, y):
    return x / y

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))