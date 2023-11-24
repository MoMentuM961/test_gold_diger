import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_scrapy_mixing.settings')

celery = Celery('django_scrapy_mixing')
celery.config_from_object('django.conf:settings', namespace='CELERY')
celery.autodiscover_tasks()

