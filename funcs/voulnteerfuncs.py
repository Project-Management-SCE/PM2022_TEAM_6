import sys
sys.path.append('../')
from voulnteers.models import volnteer
def addvoulnteer(name,email,psw):
    ex=volnteer(username=name,password=psw,email=email)
    ex.save()
    ex.is_verfied = False
    return ex

# def loadinfo():
    