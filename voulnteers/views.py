import sys
from django.contrib.auth import authenticate
from django.core.mail import EmailMessage
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.urls import reverse
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from funcs.managerfuncs import getfullschools, requestnondub, getcoords
from manager.models import School, schoolrequest, feedbacks, volinstances
from voulnteers.templatetags.vol_funcs import setname, setpfp,setactive
from datetime import datetime

from . import models
from .forms import CreateNewVoulnteer, LoginVoulnteer
from voulnteers.models import volnteer
from voulnteers.utils import token_generator
from funcs.managerfuncs import getschools

sys.path.append('../')
from funcs.voulnteerfuncs import addvoulnteer, checkpic

sys.path.append('/voulnteers')

import pytz


# test

# Create your views here.
def logoutvoulnteer(request):
    try:
        del request.session['voulnteerkey']
    except:
        pass
    return render(request, "voulnteers/logout.html", {})


def index1(response):
    if response.session.has_key('voulnteerkey'):
        return redirect('/voulnteer/mainpage')
    return redirect('/voulnteer/login')


def createaccount(response):
    message = "'Please fill the sign-up page'"
    if response.method == "POST":
        message = "'Please fill the sign-up page'"
        form = CreateNewVoulnteer(response.POST)
        if form.is_valid():
            name = form.cleaned_data["username"]
            emaill = form.cleaned_data["email"]
            psw = form.cleaned_data["password"]
            if volnteer.objects.filter(username=form.cleaned_data["username"]):
                message = 'that username exists on the site'
                return render(response, "voulnteers/createanaccount.html", {"form": form, 'message': message})
            user = addvoulnteer(name, emaill, psw)
            email_subject = 'Account_activation'
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            domain = get_current_site(response).domain
            link = reverse('activate', kwargs={"uidb64": uidb64, 'token': token_generator.make_token(user)})
            activate_url = 'http://' + domain + link
            email_body = ' Hi ' + user.username + " Please use this link to verify your account\n\n\n" + activate_url
            email = EmailMessage(
                email_subject,
                email_body,
                'noreply@voulnteering.com',
                [emaill],
            )
            email.send(fail_silently=False)
            message = "a message was sent to your email!! "

            if not user.is_verfied:
                pass

    form = CreateNewVoulnteer()
    return render(response, "voulnteers/createanaccount.html", {"form": form, 'message': message})


def loginaccount(response):
    form = LoginVoulnteer(response.POST)
    message = "please login"
    if response.session.has_key('voulnteerkey'):
        return redirect('/voulnteer/mainpage')
    if form.is_valid():
        k = authenticate(response, username=form.cleaned_data["username"], psw=form.cleaned_data["password"])
        user = volnteer.objects.get(username=form.cleaned_data["username"])
        if not user.is_verfied:
            message = "you are not verfied"
            return render(response, "voulnteers/loginaccount.html", {"form": form, 'message': message})

        if k:
            response.session['voulnteerkey'] = form.cleaned_data["username"]
            return redirect('/voulnteer/mainpage')

        return render(response, "voulnteers/loginaccount.html", {"form": form, 'message': message})

        message = k
        print(k)
    return render(response, "voulnteers/loginaccount.html", {"form": form, 'message': message})


def mainpage1(response):
    user = volnteer.objects.get(username=response.session['voulnteerkey'])
    setname(user.username)
    setpfp(user.pfp)
    if response.session.has_key('voulnteerkey'):
        return render(response, "voulnteers/mainpage.html", {})
    return redirect('/voulnteer/login')


def showschools(response):
    if not response.session.has_key('voulnteerkey'):
        return redirect('/voulnteer/login')
    usr = volnteer.objects.get(username=response.session['voulnteerkey'])
    sch = getschools(usr.id)
    return render(response, "voulnteers/show_schools.html", {'sch': sch})


def schoolinfo(response, id):
    sch = School.objects.get(coord_id=id)
    return render(response, "voulnteers/specific_school.html", {'sch': sch})


def requestpage(response):
    sch = getfullschools()
    message = 'choose a school'
    if response.method == "POST":
        schh = int(response.POST.get("schools"))
        if schh == -1:
            message = 'this school isn\'t valid'
            return render(response, "voulnteers/requests.html", {'sch': sch, 'message': message})
        k = volnteer.objects.get(username=response.session['voulnteerkey'])
        if requestnondub(k.id, schh):
            message = 'you already sent a request to the same school'
            return render(response, "voulnteers/requests.html", {'sch': sch, 'message': message})

        cc = schoolrequest(school_id=schh, volnteer_id=k.id, volnteer_name=k.username, accepted=False)
        cc.save()
        message = 'a request got sent!'

    return render(response, "voulnteers/requests.html", {'sch': sch, 'message': message})


def changepic1(response):
    if response.method == "POST":
        user = volnteer.objects.get(username=response.session['voulnteerkey'])
        image = response.FILES["myfile"]
        type = image.name.split('.')[1]
        if checkpic(type)==False:
            return HttpResponse("<strong>FILE FORMAT WRONG</strong>")
        user.pfp=image

        user.save()
        return redirect('/coordinator/mainpage')

    return render(response, "voulnteers/changepic.html", {})

def feedback_view1(request):
    if not request.session.has_key('voulnteerkey'):
        return HttpResponse("<strong>You are not logged.</strong>")
    user = volnteer.objects.get(username=request.session['voulnteerkey'])
    sentfeedbacks = list(feedbacks.objects.filter(sender_id=user.id))
    recievedfeedbacks = list(feedbacks.objects.filter(~Q(sender_id=user.id) & Q(is_read__in=[False])))

    return render(request, 'voulnteers/view_feedbacks.html', {'recieved': recievedfeedbacks, 'sent': sentfeedbacks})

def oldfeedbacks1(request):
    if not request.session.has_key('voulnteerkey'):
        return HttpResponse("<strong>You are not logged.</strong>")
    user = volnteer.objects.get(username=request.session['voulnteerkey'])
    recievedfeedbacks = list(feedbacks.objects.filter(~Q(sender_id=user.id) & Q(is_read__in=[True])))
    return render(request, 'voulnteers/old_feedbacks.html', {'recieved': recievedfeedbacks})


def spfeedback(request, id):
    if not request.session.has_key('voulnteerkey'):
        return HttpResponse("<strong>You are not logged.</strong>")
    feedback = feedbacks.objects.get(id=id)
    user = volnteer.objects.get(username=request.session['voulnteerkey'])
    print('**********************')
    if request.method == "POST":
        if request.POST.get("delete"):
            print('kkk')
            feedbacks.objects.get(id=id).delete()

        if request.POST.get("mark"):
            feedback.is_read=True
            feedback.save()
        return redirect('/voulnteers/viewfeedbacks')

    return render(request, 'voulnteers/spcfeedback.html', {'feedback': feedback, 'currentid': user.id})

def send_feedback(response):
    if not response.session.has_key('voulnteerkey'):
        return HttpResponse("<strong>You are not logged.</strong>")
    message = ''
    user = volnteer.objects.get(username=response.session['voulnteerkey'])
    coords = getcoords(user.id)

    if response.method == "POST":
        urgency = response.POST.get("urgency")
        users = response.POST.get("users")
        text = response.POST.get("textarea")
        header = response.POST.get("header")

        print(text)
        if urgency == 'urgent':
            urg = True
        else:
            urg = False
        c = feedbacks(text=text, header=header, urg=urg, sender_id=user.id, reciever_id=int(users),
                      timesent=datetime.now())
        c.save()
        message = 'a feedback was sent!'
    return render(response, 'voulnteers/send_feedback.html', {'coords': coords, 'message': message})

class VerficationView(View):
    def get(self, request, uidb64, token):
        try:

            id = force_str(urlsafe_base64_decode(uidb64))
            user = volnteer.objects.get(pk=id)
            print(id)

            if not token_generator.check_token(user, token):
                return HttpResponse("<strong>You are already activated.</strong>")

            if user.is_verfied:
                return HttpResponse("<strong>You are Already verfied.</strong>")
            user.is_verfied = True
            user.save()
            print("sucess")

            return HttpResponse("<strong>You got verfied </strong>")

        except Exception as ex:
            print("test")
            pass

        return redirect('login')

def removeuser(response):
    try:
        del response.session['voulnteerkey']
    except:
        pass
    form = LoginVoulnteer(response.POST)
    message = "are you shure you want to delete youre account"
    if form.is_valid():
        user = volnteer.objects.get(username=form.cleaned_data["username"])
        if not user.is_verfied:
            message = "you are not verfied"
            return render(response, "voulnteers/removeuser.html", {"form": form, 'message': message})
        volnteer.objects.filter(username=form.cleaned_data["username"]).delete()
        return render(response, "voulnteers/remove.html", {"form": form, 'message': message})

    return render(response, "voulnteers/removeuser.html", {"form": form, 'message': message})


def online(response):
    user = volnteer.objects.get(username=response.session['voulnteerkey'])
    if (user.online==False):
        user.online=True
        setactive("checked")
        user.save()
        message="you are online"
    elif (user.online == True):
        user.online = False
        setactive("unchecked")
        user.save()
        message = "you are offline"

    return redirect(response.META.get('HTTP_REFERER'))

def spf_event(response,schoolid,eventid):
    user = volnteer.objects.get(username=response.session['voulnteerkey'])
    eventt=volinstances.objects.get(id=eventid)
    return render(response, 'voulnteers/event.html', { 'currentid': user.id,'event':eventt})

def show_events(response,schoolid):
    utc = pytz.UTC
    user = volnteer.objects.get(username=response.session['voulnteerkey'])
    sch=School.objects.get(id=schoolid)

    completed = Q(complete__in=[False])
    matchschool = Q(school_id=schoolid)
    events = list(volinstances.objects.filter(completed & matchschool))
    curtime=datetime.now()
    curtime=utc.localize(curtime)
    for i in events:
        if i.endttime < curtime:
            print(curtime,i.endttime)
            i.complete=True
            i.save()
    completed = Q(complete__in=[False])
    matchschool = Q(school_id=schoolid)
    events = list(volinstances.objects.filter(completed & matchschool))
    c=[]
    for i in events:
        if user in i.volnteers.all():
            c.append(i)
    return render(response, 'voulnteers/show_school_events.html', {'events': c,'school':sch})





