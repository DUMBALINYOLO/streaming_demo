from __future__ import unicode_literals, absolute_import
import os
from django.conf import settings
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')

app = Celery('demo')


app.config_from_object('django.conf:settings',namespace='CELERY')

app.conf.beat_schedule = {
    'stream_finance': {
        "task": "stream.tasks.stream_finance",
        "schedule": 0.1
    }

}

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)