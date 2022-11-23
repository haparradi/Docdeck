from django.shortcuts import render
from .models import BlogPosts
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404


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


