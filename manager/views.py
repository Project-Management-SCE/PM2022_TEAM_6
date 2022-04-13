from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from funcs.managerfuncs import get_data

from voulnteers.forms import LoginVoulnteer


# Create your views here.

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
    return render(response, "manager/base.html", {})


def logoutUser(request):
    try:
        del request.session['managerkey']
    except:
        pass
    return HttpResponse("<strong>You are logged out.</strong>")
