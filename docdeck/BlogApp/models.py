from django.db import models
from django.utils import timezone
from LoginApp.models import Doctor
from django.template.defaultfilters import slugify

class Category(models.Model):
    
    name_blog = models.CharField(max_length=100)

    def __str__(self):
        return self.name_blog

class BlogPosts(models.Model):

    class PostObjects(models.Manager):
        
        def get_queryset(self):
            return super().get_queryset() .filter(status="published")

    options  = (
    
        ("draft" , "Draft"),    
        ("published" , "Published")

    )
            
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    post_image = models.ImageField(null=True, blank=True, upload_to = 'media/', default="default_avatar.jpg")
    post_title = models.CharField(max_length=400)
    post_description = models.TextField(null=True)
    post_content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date="published", null=False, unique= True)
    published = models.DateField(default=timezone.now)
    author = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="blog_post")
    status = models.CharField(max_length=10, choices=options, default="draft")
    objects = models.Manager()
    postobjects = PostObjects

    class Meta:
        ordering = ("-published",)
        
    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.post_title)
        return super().save(*args, **kwargs)

class Comments(models.Model): 
    post = models.ForeignKey(BlogPosts, on_delete=models.CASCADE, related_name="comments")
    comment_name = models.CharField(max_length=40)
    comment_email = models.EmailField()
    comment_content = models.TextField(max_length=1000)
    publish = models.DateField(auto_now_add=True)
    comment_status = models.BooleanField(default=True)