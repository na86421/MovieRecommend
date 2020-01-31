from django.db import models
from imagekit.models.fields import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings
#from django.contrib.auth.models import User

from django.db.models.signals import post_save  
from django.dispatch import receiver

from django.contrib.auth.models import AbstractUser
"""
class Impot(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=40, blank =True)
    introduction = models.TextField(blank=True)
    image = ProcessedImageField(
    		blank = True,
        	upload_to = 'profile/images',
        	processors = [ResizeToFill(300, 300)],
        	format = 'JPEG',
        	options = {'quality':90},
    		)
			
class Signuser(models.Model):
	
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    selected = models.TextField(max_length=500)
"""

class User(AbstractUser):
    selected1=models.CharField(settings.AUTH_USER_MODEL, max_length=99999)
    selected2=models.CharField(settings.AUTH_USER_MODEL, max_length=99999)
    selected3=models.CharField(settings.AUTH_USER_MODEL, max_length=99999)
    selected4=models.CharField(settings.AUTH_USER_MODEL, max_length=99999)
    selected5=models.CharField(settings.AUTH_USER_MODEL, max_length=99999)
    user_comment = models.TextField(settings.AUTH_USER_MODEL,max_length=300, blank=True)
    photo = models.ImageField(settings.AUTH_USER_MODEL,upload_to='static/',
        default='/1.jpg')     

class Users(models.Model):
	
    name=models.CharField(max_length =50)
    email=models.EmailField()
    title=models.CharField(max_length =50)
    comment=models.TextField(max_length=500)
    def __str__(self):
        return self.title


#class Signuser(models.Model):
	
#	username= models.CharField(max_length=50)
#	password= models.CharField(max_length=50)
#	email= models.EmailField()
	#selected= models.TextField(max_length=500)
  #  def __str__(self):
   #     return self.username

	
	
	
	
	