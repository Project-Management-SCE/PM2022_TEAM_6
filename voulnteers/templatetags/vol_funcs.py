from django import template
from funcs.managerfuncs import getpicname
from funcs.voulnteerfuncs import getvolname

register = template.Library()

c = 'test'
profpic = ''


def setname(l):
    global c
    c = l


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
