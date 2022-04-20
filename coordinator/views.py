from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from funcs.managerfuncs import getvols
from voulnteers.forms import LoginVoulnteer
from voulnteers.models import volnteer
from manager.models import School, schoolrequest, messegerequest
from django.db.models import Q

# Create your views here.

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .forms import CreateUserForm
from .models import *


def index(response):
    if response.session.has_key('coorkey'):
        return redirect('/coordinator/mainpage')
    return redirect('/coordinator/login')


def logoutUser(request):
    try:
        del request.session['coorkey']
    except:
        pass
    return HttpResponse("<strong>You are logged out.</strong>")


def loginaccount(response):
    form = LoginVoulnteer(response.POST)
    message = "please login"
    if response.session.has_key('coorkey'):
        return redirect('/coordinator/mainpage')
    if form.is_valid():
        k = authenticate(response, username=form.cleaned_data["username"], psw=form.cleaned_data["password"])
        user = volnteer.objects.get(username=form.cleaned_data["username"])
        if k:
            response.session['coorkey'] = form.cleaned_data["username"]
            return redirect('/coordinator/mainpage')

        return render(response, "coordinator/loginaccount.html", {"form": form, 'message': message})

        message = k
        print(k)
    return render(response, "coordinator/loginaccount.html", {"form": form, 'message': message})


def school_requests(response):
    coor = volnteer.objects.get(username=response.session['coorkey'])
    requestss = list(schoolrequest.objects.filter(Q(school_id=coor.school_id) & Q(accepted=False)))
    print(requestss)
    if response.method == "POST":
        req = response.POST.get("agree_on").split(',')
        print(req)
        volnteerid = int(req[0])
        schid = int(req[1])
        print(volnteerid, '***', schid)
        voll = Q(volnteer_id=volnteerid)
        schh = Q(school_id=schid)
        c = schoolrequest.objects.get(voll & schh)
        c.accepted = True
        c.save()

    return render(response, "coordinator/school_requests.html", {'schreq': requestss})


def urgentreq(response):
    coor = volnteer.objects.get(username=response.session['coorkey'])
    urg = list(messegerequest.objects.filter(volid=coor.id))
    if response.method == "POST":
        mark = int(response.POST.get("mark"))
        cc = messegerequest.objects.filter(id=mark)
        print('****', cc)
        cc.delete()
        # cc.save()

    return render(response, "coordinator/urgent_requests.html", {'urg': urg})


def showvoulnteers(response):
    coor = volnteer.objects.get(username=response.session['coorkey'])
    vol = getvols(coor.school_id)
    return render(response, "coordinator/show_voulnteers.html", {'vol': vol})


def mainpage(response):
    if not response.session.has_key('coorkey'):
        return redirect('/coordinator/login')
    coord = volnteer.objects.get(username=response.session['coorkey'])
    sch = School.objects.get(coord_id=coord.id)

    return render(response, "coordinator/mainpage.html", {'coord': coord, 'sch': sch})
