# coding=utf-8
from __future__ import absolute_import

## Broker settings.
broker_url = 'amqp://guest:guest@localhost//'

# List of modules to import when celery starts.
imports = ('pworker.task.tasks', 'pworker.task.sched_tasks')

## Using the database to store task state and results.
# :see http://docs.celeryproject.org/en/latest/userguide/configuration.html#conf-database-result-backend
####
#    SQL CONFIG
####
SQL_CONFIG_HOST = '1.1.1.8' if not DEBUG else '192.168.1.12'
SQL_CONFIG_PORT = 3306
SQL_CONFIG_DB = 'db2'
SQL_CONFIG_USER = 'celery' if not DEBUG else 'root'
SQL_CONFIG_PASSWD = 'celery' if not DEBUG else 'rootpasswd'

result_backend = 'db+mysql://{user}:{password}@{host}/{dbname}'\
                            .format(user=SQL_CONFIG_USER, password=SQL_CONFIG_PASSWD,
                                    host=SQL_CONFIG_HOST, dbname=SQL_CONFIG_DB)

# task_annotations
# https://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-task_annotations
# task_annotations = {'pworker.tasks.sendReceiptMail': {'rate_limit': '10/s'}}  # 10 tasks a second


##
# this is for celery beat
#
## timezone setting
# https://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-timezone

enable_utc = True # Asia/Seoul is +9:00
timezone='UTC'

from datetime import timedelta

beat_schedule = {
    'add-every-30-seconds': {
        'task': 'pworker.task.tasks.add',
        'schedule': timedelta(seconds=30),
        'args': (16, 16)
    },
}
# beat_scheduler = "pworker.scheduler.sqlalchemy_scheduler:DatabaseScheduler"