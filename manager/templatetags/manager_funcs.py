from django import template
from funcs.managerfuncs import getpicname
from  funcs.voulnteerfuncs import getvolname
register = template.Library()

@register.filter(name='showpic')
def showpic(value):
    return getpicname()

@register.filter(name='getname')
def volname(value):
    if int(value)==-1:
        return 'Admin'
    return getvolname(int(value))
