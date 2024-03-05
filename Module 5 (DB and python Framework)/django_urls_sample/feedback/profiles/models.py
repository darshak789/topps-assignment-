from django.db import models

# Create your models here.

class UserProfile(models.Model):
    #image=models.FileField(upload_to='images') #set the media_root settings.
    image=models.ImageField(upload_to='images')
