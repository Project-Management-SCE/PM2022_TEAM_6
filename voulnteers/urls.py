from django.urls import path
from . import views
from .views import VerficationView
urlpatterns= [
    path("",views.index,name="index"),
    path("create", views.createaccount, name="createaccount"),
    path("login", views.loginaccount, name="loginaccount"),
    path("mainpage", views.mainpage, name="mainpage"),
    path("request", views.requestpage, name="request"),
    path("schools", views.showschools, name="schools"),
    path("logout", views.logoutvoulnteer, name="logoutvoulnteer"),
    path('activate/<uidb64>/<token>',VerficationView.as_view(),name="activate"),
    path('schools/<int:id>', views.schoolinfo, name="schoolinfo"),

]