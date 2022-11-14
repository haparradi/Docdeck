from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from LoginApp.forms import UpdateUserForm, UpdateProfileForm, ChangePasswordForm

# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html')

def profile(request):
    user_form = UpdateUserForm(instance=request.user)
    profile_form = UpdateProfileForm(instance=request.user.profile)
    password_form = ChangePasswordForm(request.user)
    return render(request, 'users-profile.html', {'user_form':user_form, 'profile_form':profile_form, 'password_form':password_form})

def records(request):
    return render(request, 'records.html')

def patients(request):
    return render(request, 'patients.html')