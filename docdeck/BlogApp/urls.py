from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.Blog.as_view() , name='blog'),
    path('<slug:post>/', views.post_details, name="post")
]