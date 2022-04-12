from django.contrib.auth import authenticate
from django.core.mail import EmailMessage
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from django.urls import reverse
from django.utils.encoding import force_bytes,force_str,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from .forms import CreateNewVoulnteer,LoginVoulnteer
from voulnteers.models import volnteer
from voulnteers.utils import token_generator
import sys
sys.path.append('../')
from funcs.voulnteerfuncs import addvoulnteer
sys.path.append('/voulnteers')
# Create your views here.
def logoutvoulnteer(request):
   try:
      del request.session['voulnteerkey']
   except:
      pass
   return HttpResponse("<strong>You are logged out.</strong>")
def index(response):
    return HttpResponse("TESSST")

def createaccount(response):
    message = "'Please fill the sign-up page'"
    if response.method=="POST":
        message="'Please fill the sign-up page'"
        form=CreateNewVoulnteer(response.POST)
        if form.is_valid():
            name=form.cleaned_data["username"]
            emaill=form.cleaned_data["email"]
            psw=form.cleaned_data["password"]
            if  volnteer.objects.filter(username=form.cleaned_data["username"]):
                message='that username exists on the site'
                return render(response, "voulnteers/createanaccount.html", {"form": form,'message':message})
            user=addvoulnteer(name,emaill,psw)
            email_subject='Account_activation'
            uidb64=urlsafe_base64_encode(force_bytes(user.pk))
            domain=get_current_site(response).domain
            link=reverse('activate',kwargs={"uidb64":uidb64,'token':token_generator.make_token(user)})
            activate_url='http://'+domain+link
            email_body=' Hi '+user.username+" Please use this link to verify your account\n\n\n"+activate_url
            email = EmailMessage(
                email_subject,
                email_body,
                'noreply@voulnteering.com',
                [emaill],
            )
            email.send(fail_silently=False)
            message="a message was sent to your email!! "


            if not user.is_verfied:
                pass

    form=CreateNewVoulnteer()
    return render(response,"voulnteers/createanaccount.html",{"form":form,'message':message})

def loginaccount(response):
    form = LoginVoulnteer(response.POST)
    message="please login"
    if response.session.has_key('voulnteerkey'):
        return redirect('/voulnteer/mainpage')
    if form.is_valid():
       k=authenticate(response,username=form.cleaned_data["username"],psw=form.cleaned_data["password"])
       user=volnteer.objects.get(username=form.cleaned_data["username"])
       if not user.is_verfied:
           message="you are not verfied"
           return render(response, "voulnteers/loginaccount.html", {"form": form, 'message': message})

       if k:
           response.session['voulnteerkey'] = form.cleaned_data["username"]
           return redirect('/voulnteer/mainpage')

       return render(response, "voulnteers/loginaccount.html", {"form": form, 'message': message})


       message=k
       print(k)
    return render(response, "voulnteers/loginaccount.html", {"form": form, 'message': message})


def mainpage(response):
    return render(response,"voulnteers/mainpage.html",{})


class VerficationView(View):
   def get(self,request,uidb64,token):
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


