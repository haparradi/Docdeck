from .models import BlogPosts, Comments, Category
from django import forms

class BlogForm(forms.ModelForm):
    
    class Meta:
        model = BlogPosts
        fields = ['category','post_image','post_title','post_description','post_content','slug','published','author','status']