from django.contrib import admin
from . import models


@admin.register(models.BlogPosts)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'id', 'status', 'slug', 'author')
    prepopulated_fields = {'slug': ('post_title',),}

@admin.register(models.Comments)
class  CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'comment_name', 'comment_email', 'publish', 'comment_status')
    list_filter = ('publish', 'comment_status')
    search_fields = ('post_title', 'comment_name', 'comment_email')

admin.site.register(models.Category)


