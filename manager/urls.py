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
    path('feedback/', views.feedback_view, name='view-volunteers-feedback'),
    path('contactus/', views.contact_us, name="contactus"),
    path('contactus/<int:id>', views.contactuspage, name="contactuspage"),
    path("", index, name="index"),

]
