from django.contrib.auth import authenticate
from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateNewVoulnteer,LoginVoulnteer
from voulnteers.models import volnteer
import sys
sys.path.append('../')
from funcs.voulnteerfuncs import addvoulnteer
sys.path.append('/voulnteers')
# Create your views here.
def index(response):
    return HttpResponse("TESSST")

def createaccount(response):
    if response.method=="POST":
        message=""
        form=CreateNewVoulnteer(response.POST)
        if form.is_valid():
            name=form.cleaned_data["username"]
            email=form.cleaned_data["email"]
            psw=form.cleaned_data["password"]
            if  volnteer.objects.filter(username=form.cleaned_data["username"]):
                message='that username exists on the site'
                return render(response, "voulnteers/createanaccount.html", {"form": form,'message':message})
            user=addvoulnteer(name,email,psw)


            if not user.is_verfied:
                pass



    form=CreateNewVoulnteer()
    return render(response,"voulnteers/createanaccount.html",{"form":form,'message':'Please fill the sign-up page'})

def loginaccount(response):
    form = LoginVoulnteer(response.POST)
    message="please login"
    if form.is_valid():
       k=authenticate(response,username=form.cleaned_data["username"],psw=form.cleaned_data["password"])
       message=k
       print(k)
    return render(response, "voulnteers/loginaccount.html", {"form": form, 'message': message})

