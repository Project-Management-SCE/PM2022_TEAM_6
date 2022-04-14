from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logoutUser"),
    path('profile/', views.mainpage, name="mainpage"),
    path('addschool/', views.addschool, name="addschool"),
    path('addcoordinator/', views.add_coordinator, name="addcoordinator"),
    path('urgent/', views.urgentrequest, name="urgent"),

]
