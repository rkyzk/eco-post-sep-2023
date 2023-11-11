"""アドミンパネルをカスタマイズする"""

from django.contrib import admin
from django.db import models
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin
from datetime import datetime


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    アドミンパネルのリスト、フィルター項目をカスタマイズ
    """
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'published_on')
    summernote_fields = ('content',)
    actions = ['publish_posts']

    def feature_posts(self, request, queryset):
        """
        記事をおすすめ記事に設定する
        arguments: self, request, queryset: おすすめ記事に設定する記事
        """
        queryset.update(featured_flag=True)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """コメントモデルのリスト、フィルター項目などをカスタマイズ"""
    list_display = ('commenter', 'body', 'post',
                    'created_on', 'comment_status')
    list_filter = ('created_on', 'comment_status')
    search_fields = ('commenter', 'body')
