from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Doctor(AbstractUser):
    image = models.ImageField(null=True, blank=True, upload_to = "meida/", default="default_avatar.jpg")
    




    