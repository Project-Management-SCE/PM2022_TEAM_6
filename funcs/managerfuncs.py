
from manager.models import messegerequest
import sys
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