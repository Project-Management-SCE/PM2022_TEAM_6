from django.contrib import admin
from django.db import models
from manager.models import schoolrequest
from voulnteers.models import volnteer, School, Feedback


class school_request(admin.ModelAdmin):
    list_display = ('accepted', 'school_id', 'volnteer_id', 'volnteer_name', 'school_id')
    search_fields = ('volnteer_id', 'accepted')


class volnteer_class(admin.ModelAdmin):
    list_display = ('username', 'email', 'password', "is_verfied", 'is_coordinator', 'school_id', 'pfp')
    search_fields = ('username', 'password')


class school_class(admin.ModelAdmin):
    list_display = ('name', 'town', 'x_axis', 'y_axis', 'coord_id')
    search_fields = ('name', 'town')


class feedback_class(admin.ModelAdmin):
    list_display = ('date', 'by', 'message')
    search_fields = ('date', 'by')


admin.site.register(schoolrequest, school_request)
admin.site.register(volnteer, volnteer_class)
admin.site.register(School, school_class)
admin.site.register(Feedback, feedback_class)

# Register your models here.
