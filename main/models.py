from distutils.command.upload import upload
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone



class Profile(models.Model):
  user  = models.OneToOneField(User, on_delete=models.CASCADE)
  image = models.ImageField(default='default.png', upload_to='profile_pics', blank=True, null=True)
  
  def __str__(self):
    return self.user.username
