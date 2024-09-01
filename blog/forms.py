"""PostとCommentフォームを定義するモジュール"""

from .models import Comment, Post, CATEGORY
from django import forms
from django_yearmonth_widget.widgets import DjangoYearMonthWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field


class DateInput(forms.DateInput):
    input_type = 'date'


class PostForm(forms.ModelForm):
    """Postフォーム"""
    title = forms.CharField(label='タイトル')
    content = forms.CharField(label='内容', widget=forms.Textarea)
    featured_image = forms.ImageField(label='画像', required=False)
    city = forms.CharField(label='市/町/村')
    category = forms.CharField(label='カテゴリー')

    class Meta:
        model = Post
        fields = ['title', 'content', 'featured_image',
                  'city', 'category']


class CommentForm(forms.ModelForm):
    """コメントフォームの入力フィールド、ラベルを設定"""
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {'body': 'コメント'}
