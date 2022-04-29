from datetime import datetime
from django_jinja import library
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.db.models import Q

from django.utils import timezone
from funcs.managerfuncs import get_data,getemptyschools
from manager.models import School, messegerequest
from voulnteers.forms import LoginVoulnteer
from funcs.managerfuncs import addschooll,addcoordinator,uploadpic,getpicname


# Create your views here.
from voulnteers.models import volnteer

library.global_function(getpicname)
def loginPage(response):
    form = LoginVoulnteer(response.POST)
    message = "please login"
    if response.session.has_key('managerkey'):
        return redirect('/manager/profile')
    if form.is_valid():
        k = authenticate(response, username=form.cleaned_data["username"], psw=form.cleaned_data["password"])
        if form.cleaned_data["username"] == get_data()[0] and form.cleaned_data["password"] == get_data()[1]:
            response.session['managerkey'] = form.cleaned_data["username"]
            return redirect('/manager/profile')

        return render(response, "manager/login.html", {"form": form, 'message': message})

        message = k
        print(k)
    return render(response, "manager/login.html", {"form": form, 'message': message})


def mainpage(response):
    if not response.session.has_key('managerkey'):
      return HttpResponse("<strong>You are not logged.</strong>")
    return render(response, "manager/base.html", {})




def addschool(response):
    if not response.session.has_key('managerkey'):
      return HttpResponse("<strong>You are not logged.</strong>")
    message='fill the information and pick a location'
    if response.method=="POST":
        name = response.POST.get("name")
        town = response.POST.get("town")
        xaxis = response.POST.get("lat")
        yaxis = response.POST.get("lng")
        addschooll(name,town,xaxis,yaxis)
        message='a school is added!!'
    return render(response, "manager/add_school.html", {'message':message})


def add_coordinator(response):
    if not response.session.has_key('managerkey'):
      return HttpResponse("<strong>You are not logged.</strong>")
    message='fill the form to add a coordinator'
    emptyschools=getemptyschools()
    if response.method=="POST":
        name = response.POST.get("name")
        school_id = response.POST.get("schools")
        email = response.POST.get("email")
        psw = response.POST.get("password")
        coords= Q(is_coordinator=True)
        hasname= Q(username=name)
        if volnteer.objects.filter(coords & hasname):
           message = 'that username exists on the site'
           return render(response, "manager/add_coordinator.html", {'sch': emptyschools,'message':message})
        user=addcoordinator(name,email,psw,school_id)
        c=School.objects.get(id=school_id)
        print(c)
        print("******************************************")
        c.coord_id=user.id
        c.save()
    return render(response, "manager/add_coordinator.html", {'sch': emptyschools, 'message': message})



def logoutUser(request):
    try:
        del request.session['managerkey']
    except:
        pass
    return HttpResponse("<strong>You are logged out.</strong>")


def urgentrequest(response):
    if not response.session.has_key('managerkey'):
      return HttpResponse("<strong>You are not logged.</strong>")
    coor=volnteer.objects.filter(is_coordinator=True)
    message='fill the form'
    if response.method=="POST":
        urgency=response.POST.get("urgency")
        coorid=response.POST.get("coords")
        text=response.POST.get("textarea")

        print(text)
        if urgency=='urgent':
            urg=True
        else:
            urg=False
        c=messegerequest(text=text,header='request from the admin',urg=urg,volid=int(coorid),timesent=datetime.now())
        c.save()
        message='an urgent request was sent!'



    return render(response, "manager/urgent.html", {'coor':coor,'message':message})


def changepic(response):
    if response.method == "POST" :
        image=response.FILES["myfile"]
        fc=FileSystemStorage()
        type=image.name.split('.')[1]
        imagename="admin"+"."+type
        uploadpic(imagename)
        filename=fc.save(imagename,image)


        upload=fc.url(filename)



    return render(response, "manager/changepic.html",{'picname':getpicname()})

