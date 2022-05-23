from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.loginaccount, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path("mainpage", views.mainpage, name="mainpage"),
    path("voulnteers", views.showvoulnteers, name="voulnteers"),
    path('schoolrequests/', views.school_requests, name="schoolrequests"),
    path('urgent/', views.urgentreq, name="urgent"),
    path('changepic/', views.changepic, name="changepic"),
    path('viewfeedbacks/', views.feedback_view, name='viewfeedbacks'),
    path('oldfeedbacks/', views.oldfeedbacks, name='oldfeedbacks'),
    path('sendfeedback/', views.send_feedback, name='send-feedback'),
    path('feedback/<int:id>', views.spfeedback, name="spfeedback"),
    path('event/<int:id>', views.event, name="event"),
    path('event/', views.view_events, name="view_events"),
    path('removeuser/', views.removeuser, name="removeuser"),
    path('newinstance/', views.newinstance, name="newinstance"),


]
