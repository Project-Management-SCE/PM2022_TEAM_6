from django.urls import path
from . import views
from .views import VerficationView

urlpatterns = [
    path("", views.index1, name="index1"),
    path("create", views.createaccount, name="createaccount"),
    path("login", views.loginaccount, name="loginaccount"),
    path("mainpage", views.mainpage1, name="mainpage1"),
    path("request", views.requestpage, name="requeset"),
    path("schools", views.showschools, name="schools"),
    path("logout", views.logoutvoulnteer, name="logoutvoulnteer"),
    path('changepic/', views.changepic1, name="changepic1"),
    path('activate/<uidb64>/<token>', VerficationView.as_view(), name="activate"),
    path('schools/<int:id>', views.schoolinfo, name="schoolinfo"),
    path('viewfeedbacks/', views.feedback_view1, name='viewfeedbacks1'),
    path('oldfeedbacks/', views.oldfeedbacks1, name='oldfeedbacks1'),
    path('sendfeedback/', views.send_feedback, name='send-feedback'),
    path('feedback/<int:id>', views.spfeedback, name="spfeedback"),
    path('events/<int:schoolid>', views.show_events, name="showevents"),
    path('events/<int:schoolid>/<int:eventid>', views.spf_event, name="showevent"),
    path('removeuser/',views.removeuser,name="removeuser"),
    path('base/',views.online,name="online"),

]
