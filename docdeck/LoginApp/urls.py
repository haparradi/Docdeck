"""docdeck URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from PacientesApp.views import enviar_consulta
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('update_user', views.update_user, name='update_user'),
    path('password_change/', views.change_password, name='password_change'),
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('contact/', enviar_consulta, name='contact'),
]

htmx_views = [
    path('check_username/', views.check_username, name='check_username'),
]

urlpatterns+=htmx_views