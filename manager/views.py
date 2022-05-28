from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.core.mail import EmailMessage

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.db.models import Q

from django.utils import timezone
from funcs.managerfuncs import get_data, getemptyschools, getaboutus, changeaboutus
from funcs.voulnteerfuncs import checkpic
from manager.models import School, messegerequest, contactus, feedbacks, logs
from voulnteers.forms import LoginVoulnteer
from funcs.managerfuncs import addschooll, addcoordinator, uploadpic, getpicname

# Create your views here.
from voulnteers.models import volnteer


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
        k = logs(activity="manager login", done_by=-1, done_to=-5, activity_date=datetime.now())
        k.save()
    return render(response, "manager/login.html", {"form": form, 'message': message})


def mainpage(response):
    if not response.session.has_key('managerkey'):
        return HttpResponse("<strong>You are not logged.</strong>")
    return render(response, "manager/base.html",{})


def addschool(response):
    if not response.session.has_key('managerkey'):
        return HttpResponse("<strong>You are not logged.</strong>")
    message = 'fill the information and pick a location'
    if response.method == "POST":
        name = response.POST.get("name")
        town = response.POST.get("town")
        xaxis = response.POST.get("lat")
        yaxis = response.POST.get("lng")
        addschooll(name, town, xaxis, yaxis)
        message = 'a school is added!!'
        k = logs(activity="Adding School", done_by=-1, done_to=-5, activity_date=datetime.now())
        k.save()
    return render(response, "manager/add_school.html", {'message': message})


def add_coordinator(response):
    if not response.session.has_key('managerkey'):
        return HttpResponse("<strong>You are not logged.</strong>")
    message = 'fill the form to add a coordinator'
    emptyschools = getemptyschools()
    if response.method == "POST":
        name = response.POST.get("name")
        school_id = response.POST.get("schools")
        email = response.POST.get("email")
        psw = response.POST.get("password")
        coords = Q(is_coordinator__in=[True])
        hasname = Q(username=name)
        if volnteer.objects.filter(coords & hasname):
            message = 'that username exists on the site'
            return render(response, "manager/add_coordinator.html", {'sch': emptyschools, 'message': message})
        user = addcoordinator(name, email, psw, school_id)
        c = School.objects.get(id=school_id)
        print(c)
        print("******************************************")
        c.coord_id = user.id
        c.save()
        k = logs(activity="Adding coordinator ", done_by=-1, done_to=-5, activity_date=datetime.now())
        k.save()
    return render(response, "manager/add_coordinator.html", {'sch': emptyschools, 'message': message})


def logoutUser(request):
    try:
        del request.session['managerkey']
    except:
        pass
    return render(request, "manager/logout.html")


def urgentrequest(response):
    if not response.session.has_key('managerkey'):
        return HttpResponse("<strong>You are not logged.</strong>")
    coor = volnteer.objects.filter(is_coordinator__in=[True])
    message = 'fill the form'
    if response.method == "POST":
        urgency = response.POST.get("urgency")
        coorid = response.POST.get("coords")
        text = response.POST.get("textarea")

        print(text)
        if urgency == 'urgent':
            urg = True
        else:
            urg = False
        c = messegerequest(text=text, header='request from the admin', urg=urg, volid=int(coorid),
                           timesent=datetime.now())
        message = 'an urgent request was sent!'
        c.save()
        c = logs(activity="Sending Argent request ", done_by=-1, done_to=-5, activity_date=datetime.now())
        c.save()

    return render(response, "manager/urgent.html", {'coor': coor, 'message': message})


def changepic(response):
    if response.method == "POST":
        image = response.FILES["myfile"]
        fc = FileSystemStorage()
        type = image.name.split('.')[1]
        if checkpic(type) == False:
            return HttpResponse("<strong>FILE FORMAT WRONG</strong>")

        imagename = "admin" + "." + type
        uploadpic(imagename)
        filename = fc.save(imagename, image)

        upload = fc.url(filename)
        c = logs(activity="changing profile image ", done_by=-1, done_to=-5, activity_date=datetime.now())
        c.save()
    return render(response, "manager/changepic.html", {'picname': getpicname()})


def contact_us(request):
    if not request.session.has_key('managerkey'):
        return HttpResponse("<strong>You are not logged.</strong>")
    req = contactus.objects.all()
    return render(request, 'manager/contactus.html', {'req': req})


def last_changes(request):
    if not request.session.has_key('managerkey'):
        return HttpResponse("<strong>You are not logged.</strong>")
    last = logs.objects.all()
    return render(request, 'manager/lastChanges.html', {'last': last})


def contactuspage(request, id):
    if not request.session.has_key('managerkey'):
        return HttpResponse("<strong>You are not logged.</strong>")
    req = contactus.objects.get(id=id)
    message = ''
    if request.method == "POST":
        header = request.POST.get("header")
        text = request.POST.get("text")
        email = EmailMessage(
            header,
            text,
            'noreply@voulnteering.com',
            [req.email], )
        email.send(fail_silently=False)
        message = "you replied back!! "
        req.delete()

    return render(request, 'manager/contact_us_page.html', {'req': req, 'message': message})


def aboutus(response):
    if not response.session.has_key('managerkey'):
        return HttpResponse("<strong>You are not logged.</strong>")
    c = getaboutus()
    mainbody = c[0]
    quote = c[1]
    message = ''
    if response.method == "POST":
        quote = response.POST.get("header")
        mainbody = response.POST.get("text")
        changeaboutus(mainbody, quote)
        message = "The page got updated "
    return render(response, 'manager/aboutus.html', {'mainbody': mainbody, 'quote': quote, 'message': message})


def send_feedback(response):
    if not response.session.has_key('managerkey'):
        return HttpResponse("<strong>You are not logged.</strong>")
    message = ''
    coords = volnteer.objects.filter(is_coordinator__in=[True])
    vols = volnteer.objects.filter(Q(is_coordinator__in=[False]) & Q(is_verfied__in=[True]))
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
        c = feedbacks(text=text, header=header, urg=urg, sender_id=-1, reciever_id=int(users),
                      timesent=datetime.now())
        c.save()
        message = 'a feedback was sent!'

    return render(response, 'manager/send_feedback.html', {'coords': coords, 'vols': vols, 'message': message})


def feedback_view(request):
    if not request.session.has_key('managerkey'):
        return HttpResponse("<strong>You are not logged.</strong>")
    sentfeedbacks = list(feedbacks.objects.filter(sender_id=-1))
    recievedfeedbacks = list(feedbacks.objects.filter(~Q(sender_id=-1) & Q(is_read__in=[False])))

    return render(request, 'manager/view_feedbacks.html', {'recieved': recievedfeedbacks, 'sent': sentfeedbacks})


def oldfeedbacks(request):
    if not request.session.has_key('managerkey'):
        return HttpResponse("<strong>You are not logged.</strong>")
    recievedfeedbacks = list(feedbacks.objects.filter(~Q(sender_id=-1) & Q(is_read__in=[True])))
    return render(request, 'manager/old_feedbacks.html', {'recieved': recievedfeedbacks})


def spfeedback(request, id):
    if not request.session.has_key('managerkey'):
        return HttpResponse("<strong>You are not logged.</strong>")
    feedback = feedbacks.objects.get(id=id)
    if request.method == "POST":
        if request.POST.get("delete"):
            print('kkk')
            feedbacks.objects.get(id=id).delete()

        if request.POST.get("mark"):
            feedback.is_read = True
            feedback.save()
        return redirect('/manager/viewfeedbacks')

    return render(request, 'manager/spcfeedback.html', {'feedback': feedback, 'currentid': -1})
