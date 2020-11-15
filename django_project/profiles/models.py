from django.db import models
from django.contrib.auth.models import (
AbstractBaseUser,
)

class User(AbstractBaseUser):
    email       = models.EmailField(unique= True, max_length= 250)
    active      = models.BooleanField(default= True) # can log in
    staff       =models.BooleanField(default= False) # staff user non super user
    admin       =models.BooleanField(default=False) # superuser

    USERNAME_FIELD= 'email'

class GuestEmail(models.Model):
    email       = models.EmailField()
    active      = models.BooleanField(default = True)
    update      =models.DateTimeField(auto_now= True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email