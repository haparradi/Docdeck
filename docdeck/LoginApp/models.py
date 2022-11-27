import os
from django.db import models
from django.contrib.auth.models import AbstractUser
from phone_field import PhoneField
# Create your models here.

class Doctor(AbstractUser):
    especialidad = models.CharField(max_length=20, null=True, blank=True)
    telefono = PhoneField(null=True, blank=True)
    
    # def __str__(self):
    #     return f'{self.user.username} {self.user.especialidad}'


class Profile(models.Model):
    user = models.OneToOneField(Doctor, on_delete=models.CASCADE)

    avatar = models.ImageField(null=True, blank=True, upload_to = 'media/', default="default_avatar.jpg")
    bio = models.TextField()

    def __str__(self):
        return f'{self.user.username} {self.user.especialidad}'