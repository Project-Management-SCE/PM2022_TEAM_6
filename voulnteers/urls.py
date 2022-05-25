from django.urls import path
from . import views
from .views import VerficationView

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.createaccount, name="createaccount"),
    path("login", views.loginaccount, name="loginaccount"),
    path("mainpage", views.mainpage, name="mainpage"),
    path("request", views.requestpage, name="request"),
    path("schools", views.showschools, name="schools"),
    path("logout", views.logoutvoulnteer, name="logoutvoulnteer"),
    path('changepic/', views.changepic, name="changepic"),
    path('activate/<uidb64>/<token>', VerficationView.as_view(), name="activate"),
    path('schools/<int:id>', views.schoolinfo, name="schoolinfo"),
    path('viewfeedbacks/', views.feedback_view, name='viewfeedbacks'),
    path('oldfeedbacks/', views.oldfeedbacks, name='oldfeedbacks'),
    path('sendfeedback/', views.send_feedback, name='send-feedback'),
    path('feedback/<int:id>', views.spfeedback, name="spfeedback"),
    path('events/<int:schoolid>', views.show_events, name="showevents"),
    path('events/<int:schoolid>/<int:eventid>', views.spf_event, name="showevent"),
    path('removeuser/',views.removeuser,name="removeuser"),
    path('base/',views.online,name="online"),

]
