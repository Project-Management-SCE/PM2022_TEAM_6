from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from funcs.managerfuncs import getvols, getonlinevols
from funcs.voulnteerfuncs import idstovols
from voulnteers.forms import LoginVoulnteer
from voulnteers.models import volnteer
from manager.models import School, schoolrequest, messegerequest, feedbacks, volinstances, logs
from django.db.models import Q
from coordinator.templatetags.cor_funcs import setname, setpfp
from datetime import datetime
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
    return render(request, "coordinator/logout.html", {})


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
    requestss = list(schoolrequest.objects.filter(Q(school_id=coor.school_id) & Q(accepted__in=[False])))
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
    setname(coord.username)
    setpfp(coord.pfp)
    sch = School.objects.get(coord_id=coord.id)

    return render(response, "coordinator/mainpage.html", {'coord': coord, 'sch': sch})


def changepic(response):
    if response.method == "POST":
        user = volnteer.objects.get(username=response.session['coorkey'])
        user.pfp = response.FILES["myfile"]
        user.save()
        return redirect('/coordinator/mainpage')
    # c = logs(activity="Sending feedback ", done_by=user.id, done_to=int(users), activity_date=datetime.now())
    # c.save()

    return render(response, "coordinator/changepic.html", {})


def feedback_view(request):
    if not request.session.has_key('coorkey'):
        return HttpResponse("<strong>You are not logged.</strong>")
    user = volnteer.objects.get(username=request.session['coorkey'])
    sentfeedbacks = list(feedbacks.objects.filter(sender_id=user.id))
    recievedfeedbacks = list(feedbacks.objects.filter(~Q(sender_id=user.id) & Q(is_read__in=[False])))

    return render(request, 'coordinator/view_feedbacks.html', {'recieved': recievedfeedbacks, 'sent': sentfeedbacks})


def oldfeedbacks(request):
    if not request.session.has_key('coorkey'):
        return HttpResponse("<strong>You are not logged.</strong>")
    user = volnteer.objects.get(username=request.session['coorkey'])
    recievedfeedbacks = list(feedbacks.objects.filter(~Q(sender_id=user.id) & Q(is_read__in=[True])))
    return render(request, 'coordinator/old_feedbacks.html', {'recieved': recievedfeedbacks})


def spfeedback(request, id):
    if not request.session.has_key('coorkey'):
        return HttpResponse("<strong>You are not logged.</strong>")
    feedback = feedbacks.objects.get(id=id)
    user = volnteer.objects.get(username=request.session['coorkey'])
    if request.method == "POST":
        if request.POST.get("delete"):
            print('kkk')
            feedbacks.objects.get(id=id).delete()

        if request.POST.get("mark"):
            feedback.is_read = True
            feedback.save()
        return redirect('/coordinator/viewfeedbacks')

    return render(request, 'coordinator/spcfeedback.html', {'feedback': feedback, 'currentid': user.id})


def send_feedback(response):
    if not response.session.has_key('coorkey'):
        return HttpResponse("<strong>You are not logged.</strong>")
    message = ''
    user = volnteer.objects.get(username=response.session['coorkey'])
    vols = getvols(user.school_id)
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
        c = logs(activity="Sending feedback ", done_by=user.id, done_to=int(users), activity_date=datetime.now())
        c.save()
        message = 'a feedback was sent!'
    return render(response, 'coordinator/send_feedback.html', {'vols': vols, 'message': message})


def removeuser(response):
    try:
        del response.session['coorkey']
    except:
        pass
    form = LoginVoulnteer(response.POST)
    message = "are you shure you want to delete youre account"
    if form.is_valid():
        user = volnteer.objects.get(username=form.cleaned_data["username"])
        if not user.is_verfied:
            message = "you are not verfied"
            return render(response, "coordinator/removeuser.html", {"form": form, 'message': message})
        volnteer.objects.filter(username=form.cleaned_data["username"]).delete()
        return render(response, "coordinator/remove.html", {"form": form, 'message': message})

    return render(response, "coordinator/removeuser.html", {"form": form, 'message': message})


def newinstance(response):
    if not response.session.has_key('coorkey'):
        return HttpResponse("<strong>You are not logged.</strong>")
    user = volnteer.objects.get(username=response.session['coorkey'])

    if response.method == "POST":
        start = response.POST.get("start")
        end = response.POST.get("end")
        text = response.POST.get("textarea")
        header = response.POST.get("header")
        onoff = response.POST.get("flipswitch")
        k = volinstances(starttime=start, endttime=end, cor_id=user.id, school_id=user.school_id, title=header,
                         description=text)
        k.save()
        if onoff:
            k.volnteers.set(getonlinevols(user.school_id))
        else:
            k.volnteers.set(getvols(user.school_id))
        k.save()
    return render(response, "coordinator/newinstance.html")


def event(request, id):
    user = volnteer.objects.get(username=request.session['coorkey'])
    eventt = volinstances.objects.get(id=id)
    vols = eventt.volnteers.all()
    print("*****", vols, "******")
    return render(request, 'coordinator/event.html', {'currentid': user.id, 'event': eventt, 'vols': vols})


def coord_last_changes(request):
    if not request.session.has_key('coorkey'):
        return HttpResponse("<strong>You are not logged.</strong>")
    user = volnteer.objects.get(username=request.session['coorkey'])
    last = logs.objects.filter(done_by=user.id)
    return render(request, 'coordinator/CoordLastChanges.html', {'last': last})
def view_events(request):
    if not request.session.has_key('coorkey'):
        return HttpResponse("<strong>You are not logged.</strong>")
    user = volnteer.objects.get(username=request.session['coorkey'])
    events = list(volinstances.objects.filter(school_id=user.school_id))

    return render(request, 'coordinator/showinstances.html', {'events': events})

def modify(response, id):
    user = volnteer.objects.get(username=response.session['coorkey'])
    eventt=volinstances.objects.get(id=id)
    vols=getvols(user.school_id)
    if response.method == "POST":
        start = response.POST.get("start")
        end = response.POST.get("end")
        text = response.POST.get("textarea")
        header = response.POST.get("header")
        eventt.starttime=datetime.strptime(start,"%Y-%m-%dT%H:%M")
        eventt.endttime=datetime.strptime(end,"%Y-%m-%dT%H:%M")
        eventt.title=header
        eventt.description=text
        k=idstovols(response.POST.getlist("volk"))
        eventt.volnteers.set(k)
        eventt.save()
    return render(response, 'coordinator/modify.html', { 'currentid': user.id,'event':eventt,'vols':vols})

def deleteevent(response,id):
    eventt=volinstances.objects.get(id=id)
    eventt.delete()
    return redirect('/coordinator/event/')
