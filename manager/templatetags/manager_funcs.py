from django import template
from funcs.managerfuncs import getpicname
register = template.Library()

@register.filter(name='showpic')
def showpic(value):
    return getpicname()