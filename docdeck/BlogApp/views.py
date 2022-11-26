from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.core.paginator import Paginator

from .models import BlogPosts, Comments
from .forms import BlogForm, CommentForm

from django.views.generic import TemplateView, DetailView
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin


class Blog(TemplateView):
    template_name = "blog.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = BlogPosts.objects.all()
        return context


def post_details(request, post):
    post = get_object_or_404(BlogPosts, slug=post)
    context = {'post': post}
    return render(request,"blog-single.html", context) 


# class NewPost(FormView, LoginRequiredMixin):
#     form_class = BlogForm
#     template_name = 'new-post.html'
#     success_url = reverse_lazy('index')
    
#     def form_valid(self, form):
        
def new_post(request):
    if request.method == 'POST':
       
        form = BlogForm(request.POST, request.FILES)
        
        if form.is_valid():
            data = form.cleaned_data
            post = BlogPosts.objects.create(
                category=data['category'],
                post_image=data['post_image'],
                post_title=data['post_title'],
                post_description=data['post_description'],
                post_content=data['post_content'],
                status=data['status'],
                author=request.user
            )
           
            # post.save()
            # post.author.set(request.user.id)
            post.save
            return redirect('index')
        return render(request, 'new-post.html', {'form':form})
    else:
        form = BlogForm()
        return render(request, 'new-post.html', {'form':form})
        
def new_comment(request, pk):
    if request.method == 'POST':
        
        form = CommentForm(request.POST)
        post = BlogPosts.objects.get(pk=pk)
        if form.is_valid():
            data = form.cleaned_data
            comment = Comments.objects.create(comment_name=data['comment_name'],
                                              comment_email=data['comment_email'],
                                              comment_content=data['comment_content'],
                                              post=post,
                                              )
            comment.save()
            return redirect('index')
        return render(request, 'new-comment.html', {'form':form, 'pk':pk})
    else:
        form = CommentForm()
        return render(request, 'new-comment.html', {'form':form, 'pk':pk})
    
class PostDetail(DetailView):
    model = BlogPosts
    template_name = 'post-detail.html'
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'post'