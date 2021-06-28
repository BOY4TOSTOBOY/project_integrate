# -*- coding: utf-8 -*-
from celery import Celery
from .celery_app import app as celery_app

__all__ = ['celery_app']
