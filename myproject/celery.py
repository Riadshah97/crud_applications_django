from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Create the Celery app
app = Celery('myproject')

# Load task modules from all registered Django apps
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

# Optional: Add periodic tasks directly in the Celery configuration
app.conf.beat_schedule = {
    'say-hello-every-hour': {
        'task': 'myapp.tasks.say_hello',
        'schedule': crontab(minute=0, hour='*'),  # Executes every hour
    },
}
