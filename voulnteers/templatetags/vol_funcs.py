from django import template
from funcs.managerfuncs import getpicname
register = template.Library()
def gname(i):
    c = ''
    def getname():
        return c
    if i=='get':
        return getname
    def setname(l):
        c=l

    if i=='set':
        return setname

username=''
@register.filter(name='loadname')
def loadname(value):
    return gname('get')()