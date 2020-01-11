import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 'mtgfantasydjango.conf.environments.vagrant')

app = Celery('mtgfantasydjango_celery')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Set up recurring tasks
app.conf.beat_schedule = {}