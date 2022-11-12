from django.db import models
from django.contrib.auth.models import AbstractUser
from phone_field import PhoneField
# Create your models here.

class Doctor(AbstractUser):
    especialidad = models.CharField(max_length=20, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to = "meida/", default="default_avatar.jpg")
    telefono = PhoneField(null=True, blank=True)




    