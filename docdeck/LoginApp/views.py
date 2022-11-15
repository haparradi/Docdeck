from django.shortcuts import render, redirect
import os
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Doctor
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, get_user_model, authenticate
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import FormView
from .forms import RegisterForm, UpdateUserForm, UpdateProfileForm, ChangePasswordForm

# Create your views here.
def login_user(request):
    if request.method == 'POST':
        my_form = AuthenticationForm(request, data=request.POST)
        if my_form.is_valid():
            data = my_form.cleaned_data
            user = data['username']
            pwd = data['password']
            
            user_auth = authenticate(username = user, password = pwd)
            
            if user_auth:
                login(request, user_auth)
                response = f'Welcome Dr. {user}'
                return redirect('index')
            else:
                response = 'User name or password are invalid'
                return render(request, 'index.html', {'response':response})
            
        response = 'User name or password are invalid'
        return render(request, 'index.html', {'response':response})
    else:
        my_form = AuthenticationForm()
        return render(request, 'login.html', {'my_form':my_form})
    
class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()  # save the user
        return super().form_valid(form)


def check_username(request):
    username = request.POST.get('username')
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse('<div style="color: red;"> This username already exists </div>')
    else:
        return HttpResponse('<div style="color: green;"> This username is available </div>')

@login_required
def update_user(request):
    if request.method=='POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)     
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Perfil Actualizado')
            return redirect('index')
        
        return render(request, 'users-profile.html', {'user_form':user_form , 'mensaje':'Formulario invalido'})
    else:
        return redirect('index')

def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if data['new_password1'] == data['new_password2']:                
                form.save()
            messages.success(request, "Your password has been changed")
            return redirect('login')
    pass


def home(request):
    return render(request, 'home.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def about(request):
    return render(request, 'about.html')

def team(request):
    return render(request, 'team.html')