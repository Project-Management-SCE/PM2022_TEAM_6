from celery import Celery, shared_task
from School.celery import app
from time import sleep

@shared_task
def sleepy(duration):
    sleep(duration)
    print('test')
    return 'kk'