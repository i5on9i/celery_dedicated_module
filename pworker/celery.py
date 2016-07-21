# coding=utf-8

from __future__ import absolute_import

from celery import Celery

# app = Celery('pworker',
#              broker='amqp://guest@localhost//',
#              backend='amqp://',
#              include=['pworker.tasks'])

app = Celery('pworker')

# Optional configuration, see the application user guide.
app.config_from_object('pworker.celconfig')
app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
)

if __name__ == '__main__':
    app.start()