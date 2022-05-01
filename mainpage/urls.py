from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contactus/", views.contact_us, name="contactus"),
    path("aboutus/", views.about_us, name="aboutus"),

]
