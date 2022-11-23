# imports
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, SetPasswordForm
from .models import Doctor, Profile
from django import forms

# forms
class RegisterForm(UserCreationForm):
    class Meta:
        model = Doctor
        fields = ["username", "email", "password1", "password2"]
        
class UpdateUserForm(UserChangeForm):
    
    class Meta:
        model = Doctor        
        fields = ['first_name', 'last_name', 'email', 'especialidad', 'telefono']
        help_text = {k: "" for k in fields}
        
class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    
    class Meta():
        model = Profile
        fields = ['avatar', 'bio']

class ChangePasswordForm(SetPasswordForm):
    
    class Meta:
        model = Doctor
        fields = ['current_password', 'new_password1', 'new_password2']