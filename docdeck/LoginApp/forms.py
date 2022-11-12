# imports
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import Doctor
from django import forms

# forms
class RegisterForm(UserCreationForm):
    class Meta:
        model = Doctor
        fields = ["username", "password1", "password2"]
        
class UpdateUserForm(UserChangeForm):
    
    
    class Meta:
        model = Doctor        
        fields = ['username', 'first_name', 'last_name', 'email', 'especialidad', 'image', 'telefono']
        help_text = {k: "" for k in fields}