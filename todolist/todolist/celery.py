import os
import datetime

from celery import Celery
from django.core.mail import send_mail

from tasks.models import Task

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todolist.settings')

app = Celery('todolist')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(name='send_task_reminder')
def send_task_reminder(task):
    send_mail(
        'Напоминание о задаче',
        f'Не забудьте выполнить задачу: {task.name}',
        'from@example.com',
        ['to@example.com'],
        fail_silently=False,
    )


@app.task(name='check_tasks_date')
def check_tasks_date():
    tasks_today = list(
        Task.objects.filter(execution_date=datetime.datetime.today(),
                            complete=False)
    )
    for task in tasks_today:
        send_task_reminder.delay(task)
