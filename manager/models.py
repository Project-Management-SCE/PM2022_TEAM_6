from django.db import models

# Create your models here.

class messegerequest(models.Model):
    text=models.CharField(max_length=400)
    header=models.CharField(max_length=200)
    urg=models.BooleanField()
    volid=models.IntegerField(default=-1)
    def __str__(self):
        return self.text
    def __str__(self):
        return self.urg


class School(models.Model):
    name=models.CharField(max_length=200)
    town=models.CharField(max_length=200)
    x_axis=models.FloatField()
    y_axis=models.FloatField()
    coord_id=models.FloatField()
