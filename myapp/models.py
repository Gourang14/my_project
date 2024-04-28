from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User,AbstractUser
from django.contrib.auth.models import Permission
from django.utils.translation import gettext as _
from django.conf import settings
# Create your models here.
class contact(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  email = models.EmailField(max_length=254)
  phone = models.CharField(max_length=20)
  message = models.TextField()
  date = models.DateTimeField(default=timezone.now)


 

class login(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        verbose_name=_('user'),  # Change verbose_name to 'user'
        related_name='customuser_logins'  # Change related_name to avoid clash
    )
    user_permissions=models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='customuser_user_permissions'
    )