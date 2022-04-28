from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('login/', views.loginaccount, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path("mainpage", views.mainpage, name="mainpage"),
    path("voulnteers", views.showvoulnteers, name="voulnteers"),
    path('schoolrequests/', views.school_requests, name="schoolrequests"),
    path('urgent/', views.urgentreq, name="urgent"),
    path('changepic/', views.changepic, name="changepic"),

]
