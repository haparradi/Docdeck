from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Blog.as_view() , name='blog'),
    path('post/<slug:post>/', views.post_details, name="post"),
    path('new-post/', views.new_post, name='new-post'),
]