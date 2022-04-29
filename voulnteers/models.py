from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from manager.models import School


# Create your models here.
class volnteer(AbstractUser):
    is_verfied = models.BooleanField(default=False)
    is_coordinator = models.BooleanField(default=False)
    school_id = models.IntegerField(default=-1)
    # schools = models.ManyToManyField(School)
    pfp = models.ImageField(null=True, blank=True, upload_to="vols")


class Feedback(models.Model):
    date = models.DateField(auto_now=True)
    by = models.CharField(max_length=40)
    message = models.CharField(max_length=500)


def is_verfied_func(self):
    return self.is_verfied


def __str__(self):
    c = repr(self.id) + '*' + self.email + '*' + self.password + '*' + self.username
    return c
