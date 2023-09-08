"""This module holds classes to customize the admin panel."""

from django.contrib import admin
from django.db import models
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin
from datetime import datetime


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Customize the list, search and filter items of Post model
    on the admin panel.
    """
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'published_on')
    summernote_fields = ('content',)
    actions = ['publish_posts']

    def publish_posts(self, request, queryset):
        """
        Set the status to 'Published'
        and store the published date and time.
        arguments: self, request, queryset: posts to be published
        """
        queryset.update(status=1)
        queryset.update(published_on=datetime.utcnow())


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Customizes the appearance of Comment model on the admin panel."""
    list_display = ('commenter', 'body', 'post',
                    'created_on', 'comment_status')
    list_filter = ('created_on', 'comment_status')
    search_fields = ('commenter', 'body')
