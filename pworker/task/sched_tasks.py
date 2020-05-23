# coding=utf-8

from __future__ import absolute_import

from pworker.celconfig import DEBUG

from pworker.celery import app

from celery.contrib import rdb

# ############################
# Simple test task
#
@app.task(bind=True)
def xsum(self, numbers):

    return sum(numbers)
