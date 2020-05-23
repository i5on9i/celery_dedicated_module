# coding=utf-8

from __future__ import absolute_import

from pworker.celconfig import DEBUG

from pworker.celery import app


# ############################
# Simple test task
#
@app.task
def add(x, y):
    return x + y
	
@app.task(bind=True)
def xsum(self, numbers):

    return sum(numbers)
