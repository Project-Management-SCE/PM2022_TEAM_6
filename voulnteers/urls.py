from django.urls import path
from . import views
urlpatterns= [
    path("",views.index,name="index"),
    path("create", views.createaccount, name="createaccount"),
    path("login", views.loginaccount, name="loginaccount"),

]