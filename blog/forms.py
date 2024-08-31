"""PostとCommentフォームを定義するモジュール"""

from .models import Comment, Post, CATEGORY
from django import forms
from django_yearmonth_widget.widgets import DjangoYearMonthWidget


class DateInput(forms.DateInput):
    input_type = 'date'


class PostForm(forms.ModelForm):
    """Postフォーム"""

    class Meta:
        model = Post
        fields = ['title', 'content', 'featured_image',
                  'city', 'category']
        title = forms.CharField(required=True)
        content = forms.CharField(required=True)
        city = forms.CharField(required=True)

        def __init__(self, *args, **kwargs):
            """Set required flag of featured image to False."""
            self.fields['featured_image'].required = False
            super(PostForm, self).__init__(*args, **kwargs)


class CommentForm(forms.ModelForm):
    """コメントフォームの入力フィールド、ラベルを設定"""
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {'body': 'comment'}
