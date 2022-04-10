from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
# Create your models here.
class volnteer(AbstractUser):
    is_verfied=models.BooleanField(default=False)
    
    def __str__(self):
        c= self.email+ '*' +self.password+ '*' +self.username
        return c