from celery.schedules import crontab


CELERYBEAT_SCHEDULE = {
   'check_tasks_date': {
     'task': 'check_tasks_date',
     'schedule': crontab(hour=24)},
}
