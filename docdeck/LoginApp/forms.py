# imports
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import Doctor

# forms
class RegisterForm(UserCreationForm):
    class Meta:
        model = Doctor
        fields = ["username", "password1", "password2"]