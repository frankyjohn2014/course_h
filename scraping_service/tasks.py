from celery import shared_task
from celery.task import periodic_task
from celery.schedules import crontab
import os
from scraping.views import Parse
import django
