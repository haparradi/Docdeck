from .models import BlogPosts, Comments, Category

from django import forms

class BlogForm(forms.ModelForm):
    
    
    class Meta:
        model = BlogPosts
        fields = ['category','post_image','post_title','post_description','post_content','status']
        labels = {
            'category': ('Categoria'),
            'post_image': ('Agregar Imagen'),
            'post_title': ('Titulo'),
            'post_description': ('Descripcion'),
            'post_content': ('Post'),
            'status': ('Estado'),
        }
        