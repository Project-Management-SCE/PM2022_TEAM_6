from django.contrib import admin
from django.db import models
from manager.models import schoolrequest
from voulnteers.models import volnteer
class school_request(admin.ModelAdmin):
    list_display = ('accepted', 'school_id', 'volnteer_id', 'volnteer_name','school_id')
    search_fields = ('volnteer_id','accepted')

class volnteer_class(admin.ModelAdmin):
    list_display=('username','email','password','is_coordinator','school_id')
    search_fields = ('username','password')


admin.site.register(schoolrequest, school_request)
admin.site.register(volnteer, volnteer_class)


# Register your models here.
