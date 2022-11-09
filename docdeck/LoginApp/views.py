from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, get_user_model, authenticate
from django.views.generic.edit import FormView
from .forms import RegisterForm

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
    print(username)
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse('<div style="color: red;"> This username already exists </div>')
    else:
        return HttpResponse('<div style="color: green;"> This username is available </div>')

def home(request):
    return render(request, 'home.html')