# -*- coding: utf-8 -*-
import os
from mongoengine import connect


PROJECT_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)))
TEMPLATE_PATH = os.path.join(PROJECT_PATH, 'views')
STATIC_PATH = os.path.join(PROJECT_PATH, 'assets')


connect('mentorfy')
