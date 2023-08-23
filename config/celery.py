from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from django.conf import settings
from django.apps import apps

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("config",
             include=['msg_app.tasks'])

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
