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
    list_display = ('title', 'slug', 'status', 'featured_flag', 'created_on')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'published_on', 'featured_flag')
    summernote_fields = ('content',)
    actions = ['feature_posts', 'unfeature_posts']

    @admin.action(description="おすすめ記事に設定")
    def feature_posts(self, request, queryset):
        """
        記事をおすすめ記事に設定する
        arguments: self, request, queryset: おすすめ記事に設定する記事
        """
        queryset.update(featured_flag=True)

    @admin.action(description="おすすめ記事を解除")
    def unfeature_posts(self, request, queryset):
        """
        記事をおすすめ記事に解除する
        arguments: self, request, queryset: おすすめ記事を解除する記事
        """
        queryset.update(featured_flag=False)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """コメントモデルのリスト、フィルター項目などをカスタマイズ"""
    list_display = ('commenter', 'body', 'post',
                    'created_on', 'comment_status')
    list_filter = ('created_on', 'comment_status')
    search_fields = ('commenter', 'body')
