from celery import Celery
from School.celery import app



@app.on_after_configure.connect
def add_periodic(**kwargs):
    app.add_periodic_task(2.0, testt(), name='add every 10')

def testt():
    print('test')