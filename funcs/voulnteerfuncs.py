import sys

import pytz
from django.db.models import Q
from datetime import datetime
from manager.models import volinstances

sys.path.append('../')
from voulnteers.models import volnteer
def addvoulnteer(name,email,psw):
    ex=volnteer(username=name,password=psw,email=email)
    ex.save()
    ex.is_verfied = False
    return ex
def getvolname(id):
    c=volnteer.objects.get(id=id)
    return c.username

# def loadinfo():
def checkpic(type):
    list=["png","gif","webp","tiff","psd","raw","bmp","jpeg","jpg"]
    if type in list:
        return True
    return False

def idstovols(arr):
    z=[]
    for i in arr:
          z.append(volnteer.objects.get(id=i))
    return z

def getcompletedevents(schoolid):
    completed = Q(complete__in=[True])
    matchschool = Q(school_id=schoolid)
    events = list(volinstances.objects.filter(completed & matchschool))

def updateincompletedevents(schoolid):
    utc = pytz.UTC
    completed = Q(complete__in=[False])
    matchschool = Q(school_id=schoolid)
    events = list(volinstances.objects.filter(completed & matchschool))
    curtime = datetime.now()
    curtime = utc.localize(curtime)
    for i in events:
        if i.endttime < curtime:
            print(curtime, i.endttime)
            i.complete = True
            i.save()
    completed = Q(complete__in=[False])
    matchschool = Q(school_id=schoolid)
    events = list(volinstances.objects.filter(completed & matchschool))
    return events

def getincompletedevents(schoolid):
    pass

