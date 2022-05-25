from django import template

from funcs.voulnteerfuncs import getvolname
from manager.models import volinstances
register = template.Library()


c='test'
profpic=''
def setname(l):
    global c
    c = l
def setpfp(l):
    global profpic
    profpic=l




@register.filter(name='loadname')
def loadname(value):
    global c
    return c

@register.filter(name='getpic')
def getpic(value):
    global profpic
    return profpic
@register.filter(name='getname')
def volname(value):
    if int(value)==-1:
        return 'Admin'
    if int(value)==-5:
        return ''
    return getvolname(int(value))
@register.filter(name='totime')
def totime(value):
    return value.strftime("%Y-%m-%dT%H:%M")

@register.simple_tag(name='inevent')
def inevent(eventid,volid):
    ins=volinstances.objects.get(id=eventid)
    try:
        vols = ins.volnteers.get(id=volid)
        print(vols)
    except:
        return 'unchecked'

    return 'checked'


