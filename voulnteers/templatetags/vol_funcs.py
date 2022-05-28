from django import template
from funcs.managerfuncs import getpicname
from funcs.voulnteerfuncs import getvolname, getmonthhours, totalhours

register = template.Library()

c = 'test'
profpic = ''
kk="checked"
moncounter=0
totcounter=0
def setname(l):
    global c
    c = l
def setactive(l):
    global kk
    kk = l


def setpfp(l):
    global profpic
    profpic = l


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
    if int(value) == -1:
        return 'Admin'
    return getvolname(int(value))

@register.filter(name='active')
def active(value):
    return kk

@register.filter(name='resetcounter')
def resetcounter(value):
    global moncounter
    global totcounter
    moncounter=0
    totcounter=0
    return ''
@register.filter(name='getmon')
def getmon(value):
    global moncounter
    return moncounter

@register.filter(name='gettot')
def gettot(value):
    global totcounter
    return totcounter

@register.simple_tag(name='getmonthlyhours')
def getmonthlyhours(userid,schid):
    global moncounter
    k=getmonthhours(schid,userid)
    moncounter=moncounter+k
    return k

@register.simple_tag(name='gettotalhours')
def gettotalhours(userid,schid):
    global totcounter
    k=totalhours(schid,userid)
    totcounter=totcounter+k
    return k

