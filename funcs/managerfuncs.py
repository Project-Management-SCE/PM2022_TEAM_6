from django.db.models import Q

from manager.models import messegerequest, schoolrequest
from manager.models import School

import sys

from voulnteers.models import volnteer
import os
sys.path.append('../')

def get_data():
  f=open('manager/auth_data/authdata.txt')
  data=f.readlines()
  username=data[0].strip().split(':')[1]
  psw=data[1].strip().split(':')[1]

  return (username,psw)

def addmessegerequest(text1, header1, urg1,volid1):
    ms =messegerequest(text=text1, header=header1, urg=urg1,volid=volid1)
    ms.save()
    return ms

def addschooll(name,town,xaxis,yaxis):
    sc=School(name=name,town=town,x_axis=xaxis,y_axis=yaxis,coord_id=-1)
    sc.save()
    return sc

def getemptyschools():
    c=list(School.objects.all().filter(coord_id=-1))
    return c

def getfullschools():
    c=list(School.objects.all().filter(~Q(coord_id=-1)))
    return c

def addcoordinator(name,email,psw,school_id):
    ex=volnteer(username=name,password=psw,email=email,is_coordinator=True,school_id=school_id)
    ex.is_verfied = True
    ex.save()
    return ex
def getcoordinators():
    return list(volnteer.objects.filter(is_coordinator=True))

def requestnondub(vol_id,sch_id):
    k=schoolrequest.objects.filter(Q(school_id=int(sch_id)) & Q(volnteer_id=int(vol_id)))
    if k:
        return True
    return False
def getvols(schoolid):
    k=list(schoolrequest.objects.filter(Q(school_id=int(schoolid)) & Q(accepted__in=[True])))
    z=[]
    for i in k:
        z.append(volnteer.objects.get(id=i.volnteer_id))
    return z
def getschools(volid):
    k=list(schoolrequest.objects.filter(Q(volnteer_id=int(volid)) & Q(accepted__in=[True])))
    z=[]
    for i in k:
        z.append(School.objects.get(id=i.school_id))
    return z
def getcoords(volid):
    k=list(schoolrequest.objects.filter(Q(volnteer_id=int(volid)) & Q(accepted__in=[True])))
    z=[]
    for i in k:
        z.append(volnteer.objects.get(school_id=i.school_id))
    return z

def uploadpic(image):
    f = open('manager/auth_data/picname.txt','r')
    data = f.readlines()
    oldimage = data[0].strip()
    os.remove("media/"+oldimage)

    f.close()
    f=open('manager/auth_data/picname.txt','w')
    f.write(image)
    f.close()

def getpicname():
    f = open('manager/auth_data/picname.txt', 'r')
    data = f.readlines()
    oldimage = data[0].strip()
    return oldimage


def getaboutus():
    f = open('manager/about_us/aboutus.txt')
    data = f.readlines()
    mainbody = data[0].strip()
    quote = data[1].strip()
    return (mainbody, quote)


def changeaboutus(mainbody,quote):
    f = open('manager/about_us/aboutus.txt', 'w')
    f.write(mainbody)
    f.write('\n')
    f.write(quote)
    f.close()
