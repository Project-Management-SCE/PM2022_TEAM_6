from django.db import models
# Create your models here.

class messegerequest(models.Model):
    text=models.CharField(max_length=400)
    header=models.CharField(max_length=200)
    urg=models.BooleanField()
    volid=models.IntegerField(default=-1)
    timesent=models.DateTimeField()



class School(models.Model):
    name=models.CharField(max_length=200)
    town=models.CharField(max_length=200)
    x_axis=models.FloatField()
    y_axis=models.FloatField()
    coord_id=models.IntegerField()


class schoolrequest(models.Model):
    accepted=models.BooleanField()
    school_id=models.IntegerField()
    volnteer_id=models.IntegerField()
    volnteer_name=models.CharField(max_length=200)


class feedbacks(models.Model):
    is_read=models.BooleanField(default=False)
    reciever_id=models.IntegerField()
    sender_id=models.IntegerField()
    timesent=models.DateTimeField()
    text=models.CharField(max_length=400)
    header=models.CharField(max_length=200)
    urg=models.BooleanField()

class volinstances(models.Model):
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=400)
    school_id=models.IntegerField()
    cor_id=models.IntegerField()
    volnteers = models.ManyToManyField('voulnteers.volnteer', related_name='volnteer')
    starttime=models.DateTimeField()
    endttime=models.DateTimeField()


class contactus(models.Model):
    name=models.CharField(max_length=200)
    cons=models.CharField(max_length=200)
    timesent=models.DateTimeField()
    text=models.CharField(max_length=400)
    email=models.EmailField(max_length = 255)



