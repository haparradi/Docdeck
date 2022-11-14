# Imports
from django.shortcuts import redirect
# views

def home(request):
    # if request.user.is_authenticated():
    #     return redirect('index')
    # else:
        return redirect('home')