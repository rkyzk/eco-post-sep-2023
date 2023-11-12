"""PostとCommentフォームを定義するモジュール"""

from .models import Comment, Post, CATEGORY
from django import forms


class PostForm(forms.ModelForm):
    """Postフォーム"""

    class Meta:
        """Postフォームの入力フィールドトラベルを設定"""
        model = Post
        fields = ['title', 'content', 'featured_image',
                  'city', 'category']
        title = forms.CharField(required=True)
        content = forms.CharField(required=True)
        city = forms.CharField(required=True)
        labels = {'title': 'タイトル',
                  'content': '本文',
                  'featured_image': '画像',
                  'city': '市/町/村',
                  'category': 'カテゴリー'}

        def __init__(self, *args, **kwargs):
            """featured_imageプロパティを任意に設定"""
            self.fields['featured_image'].required = False
            super(PostForm, self).__init__(*args, **kwargs)


class CommentForm(forms.ModelForm):
    """コメントフォームの入力フィールド、ラベルを設定"""
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {'body': 'comment'}
