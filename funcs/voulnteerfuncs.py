import sys
sys.path.append('../')
from voulnteers.models import volnteer
def addvoulnteer(name,psw,email):
    ex=volnteer(name=name,psw=psw,email=email)
    ex.save()