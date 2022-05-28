from django.http import HttpResponse
from django.shortcuts import render
from manager.models import contactus
from datetime import datetime
from funcs.managerfuncs import getaboutus


# Create your views here.
def index(response):
    return render(response, "mainpage/home.html", {})

def contact_us(response):
    message="fill the information"
    if response.method == "POST":
        email = response.POST.get("email")
        name = response.POST.get("name")
        cons = response.POST.get("cons")

        text = response.POST.get("text")
        c = contactus(text=text, cons=cons, name=name,timesent=datetime.now(),email=email)
        c.save()
        message='Your message was sent to the Admin'

    return render(response, "mainpage/contactus.html", {'message':message})

def about_us(response):
    c=getaboutus()
    mainbody=c[0]
    quote=c[1]
    return render(response, "mainpage/About_us.html", {'mainbody':mainbody,'quote':quote})
