from django import template
from funcs.managerfuncs import getpicname

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
