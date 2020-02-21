from django.db import models
# from django.contrib.auth.models import AbstractUser

class Gallery(models.Model): 
    uploaded = models.DateTimeField(auto_now=True)
    pic = models.ImageField(upload_to='images/')