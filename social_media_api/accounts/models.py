from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='images', blank=True, null=True)
    followers = models.ManyToManyField("self", symmetrical=False, blank=True)