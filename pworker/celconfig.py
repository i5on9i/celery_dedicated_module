# coding=utf-8
from __future__ import absolute_import

## Broker settings.
BROKER_URL = 'amqp://guest:guest@localhost//'

# List of modules to import when celery starts.
CELERY_IMPORTS = ('pworker.tasks', )

## Using the database to store task state and results.
CELERY_RESULT_BACKEND = 'amqp://'

CELERY_ANNOTATIONS = {'pworker.tasks.add': {'rate_limit': '10/s'}}

from datetime import timedelta

CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
        'task': 'pworker.tasks.add',
        'schedule': timedelta(seconds=30),
        'args': (16, 16)
    },
}