import sys
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
