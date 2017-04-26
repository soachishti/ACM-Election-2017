from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    voted = models.BooleanField(default=False)
    
class Vote(models.Model):
    position = models.TextField(max_length=500, blank=False)
    vote = models.TextField(max_length=500, blank=False)
