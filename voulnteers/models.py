from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
# Create your models here.
class volnteer(AbstractUser):
    is_verfied=models.BooleanField(default=False)
    is_coordinator=models.BooleanField(default=False)
    school_id=models.IntegerField(default=-1)
    def is_verfied_func(self):
        return self.is_verfied
    def __str__(self):
        c= repr(self.id)+'*'+self.email+ '*' +self.password+ '*' +self.username
        return c