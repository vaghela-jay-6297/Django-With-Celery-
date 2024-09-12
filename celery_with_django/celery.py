from __future__ import absolute_import, unicode_literals
import os
from time import timezone
from datetime import timedelta
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_with_django.settings')

app = Celery('celery_with_django')
app.conf.enable_utc = False

app.conf.update(timezone='Asia/Kolkata')

app.config_from_object(settings, namespace='CELERY')

# celert beat settings  -> (set schedular & periodic task)
app.conf.beat_schedule = {
    'run-task-every-15-seconds':{        # schedule beat task name
        'task': 'mainapp.tasks.send_email',      # define created task name with location
        'schedule': 15,                         # execute task in every 15 sec 
        'args': ("demo@gmail.com",)          # here set default email address.
    }
}

app.autodiscover_tasks()    # automatically detect tasks.py files in apps.

@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request}")