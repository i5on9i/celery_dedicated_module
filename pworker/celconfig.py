# coding=utf-8

## Broker settings.
BROKER_URL = 'amqp://guest:guest@localhost//'

# List of modules to import when celery starts.
CELERY_IMPORTS = ('pworker.tasks', )

## Using the database to store task state and results.
CELERY_RESULT_BACKEND = 'amqp://'

CELERY_ANNOTATIONS = {'tasks.add': {'rate_limit': '10/s'}}