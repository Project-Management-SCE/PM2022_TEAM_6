from django.urls import path
from mainpage.views import index
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logoutUser"),
    path('profile/', views.mainpage, name="mainpage"),
    path('addschool/', views.addschool, name="addschool"),
    path('addcoordinator/', views.add_coordinator, name="addcoordinator"),
    path('urgent/', views.urgentrequest, name="urgent"),
    path('changepic/', views.changepic, name="changepic"),
    path('viewfeedbacks/', views.feedback_view, name='viewfeedbacks'),
    path('oldfeedbacks/', views.oldfeedbacks, name='oldfeedbacks'),
    path('sendfeedback/', views.send_feedback, name='send-feedback'),
    path('contactus/', views.contact_us, name="contactus"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('contactus/<int:id>', views.contactuspage, name="contactuspage"),
    path('feedback/<int:id>', views.spfeedback, name="spfeedback"),
    path("", index, name="index"),

]
