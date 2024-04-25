from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class contact(models.Model):
    first_name = models.CharField(max_length=122)
    last_name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

class login(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null = True,blank = True)
