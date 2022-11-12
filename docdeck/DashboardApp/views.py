from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from LoginApp.forms import UpdateUserForm

# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html')

def profile(request):
    user_form = UpdateUserForm()
    return render(request, 'users-profile.html', {'user_form':user_form})