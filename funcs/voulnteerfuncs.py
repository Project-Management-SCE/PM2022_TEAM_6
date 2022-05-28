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
    return events

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

def getincompletedevents(schoolid):
    completed = Q(complete__in=[False])
    matchschool = Q(school_id=schoolid)
    events = list(volinstances.objects.filter(completed & matchschool))
    return events


def gethours(stdate,enddate):
    print(stdate, enddate)
    if enddate<stdate:
        return 0
    else:
        tot=enddate-stdate
        return int(tot.total_seconds() /3600)

def getschoolvols(schid,volid):
    events=getcompletedevents(schid)
    vol= volnteer.objects.get(id=int(volid))
    print(vol)
    c=[]
    for i in events:
        if vol in i.volnteers.all():
            c.append(i)
    return c

def getmonthhours(schid,volid):
    utc = pytz.UTC
    curtime = datetime.now()
    curtime = utc.localize(curtime)
    events=getschoolvols(schid,volid)
    tothours=0
    for i in events:
        if i.endttime.month==curtime.month:
            tothours=tothours+gethours(i.starttime,i.endttime)

    return tothours
def totalhours(schid,volid):
    events = getschoolvols(schid, volid)
    tothours = 0
    for i in events:
      tothours = tothours + gethours(i.starttime, i.endttime)
    return tothours








