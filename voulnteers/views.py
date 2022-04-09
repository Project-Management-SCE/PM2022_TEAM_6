from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateNewVoulnteer
import sys
sys.path.append('../')
from funcs.voulnteerfuncs import addvoulnteer
# Create your views here.
def index(response):
    return HttpResponse("TESSST")

def createaccount(response):
    if response.method=="POST":
        form=CreateNewVoulnteer(response.POST)
        if form.is_valid():
            name=form.cleaned_data["name"]
            email=form.cleaned_data["email"]
            psw=form.cleaned_data["psw"]
            addvoulnteer(name,email,psw)

    form=CreateNewVoulnteer()
    return render(response,"voulnteers/createanaccount.html",{"form":form})