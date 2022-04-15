from django.db.models import Q

from manager.models import messegerequest, schoolrequest
from manager.models import School

import sys

from voulnteers.models import volnteer

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
    print(vol_id,sch_id)
    k=schoolrequest.objects.filter(Q(school_id=int(sch_id)) & Q(volnteer_id=int(vol_id)))
    if k:
        return True
    return False
