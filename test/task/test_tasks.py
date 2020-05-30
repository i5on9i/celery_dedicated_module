# coding=utf-8

import os
import sys
sys.path.append(os.path.join(os.path.dirname(
    os.path.abspath(__file__)),  '..', '..'))

import unittest
from unittest.mock import MagicMock
from unittest.mock import ANY

from gigas.celconfig import DEBUG
from gigas.celery import app
from gigas.task.tasks import xsum

class TestAddTask(unittest.TestCase):
    def setUp(self):
        self.result = xsum([3, 5])
        # self.results = self.task.get()  

    def test_addition(self):
        res = xsum([3, 5])
        self.assertEqual(res, 8)
        self.assertEqual(self.result, 8, 'result-test')
        