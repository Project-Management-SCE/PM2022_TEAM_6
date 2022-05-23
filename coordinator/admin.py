from django.contrib import admin
from django.db import models
from manager.models import schoolrequest,contactus,feedbacks,volinstances
from voulnteers.models import volnteer, School


class school_request(admin.ModelAdmin):
    list_display = ('accepted', 'school_id', 'volnteer_id', 'volnteer_name', 'school_id')
    search_fields = ('volnteer_id', 'accepted')

class contact_us(admin.ModelAdmin):
    list_display = ('name', 'email', 'cons', "text")
    search_fields = ('name', 'cons')



class volnteer_class(admin.ModelAdmin):
    list_display = ('username', 'email', 'password', "is_verfied", 'is_coordinator', 'school_id', 'pfp')
    search_fields = ('username', 'password')


class school_class(admin.ModelAdmin):
    list_display = ('name', 'town', 'x_axis', 'y_axis', 'coord_id')
    search_fields = ('name', 'town')


class feedback_class(admin.ModelAdmin):
    list_display = ('id','reciever_id', 'sender_id', 'timesent','text','header','is_read','urg')
    search_fields = ('reciever_id', 'sender_id')

class volinc_class(admin.ModelAdmin):
    list_display = ('id','title','description', 'school_id', 'cor_id','starttime','endttime')
    search_fields = ('school_id', 'cor_id')

admin.site.register(schoolrequest, school_request)
admin.site.register(volnteer, volnteer_class)
admin.site.register(School, school_class)
admin.site.register(feedbacks, feedback_class)
admin.site.register(contactus, contact_us)
admin.site.register(volinstances, volinc_class)

# Register your models here.
