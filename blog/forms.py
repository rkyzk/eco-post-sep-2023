"""PostとCommentフォームを定義するモジュール"""

from .models import Comment, Post, Expense, CATEGORY
from django import forms
from django_yearmonth_widget.widgets import DjangoYearMonthWidget


class DateInput(forms.DateInput):
    input_type = 'date'


class PostForm(forms.ModelForm):
    """Postフォーム"""

    class Meta:
        """Postフォームの入力フィールドトラベルを設定"""
        model = Expense
        fields = ['name', 'amount', 'payment_type',
                  'payment_date', 'frequency', 'start_date', 'end_date']
        name = forms.CharField(required=True)
        amount = forms.CharField(required=True)
        payment_type = forms.IntegerField(required=True)
        payment_date = forms.DateInput(format='%Y-%m-%d')
        start_date = forms.DateInput(format='%Y-%m-%d')
        end_date = forms.DateInput(format='%Y-%m-%d')

        widgets = {
            'payment_date': DateInput(),
            'start_date': DateInput(),
            'end_date': DateInput(),
        }


class CommentForm(forms.ModelForm):
    """コメントフォームの入力フィールド、ラベルを設定"""
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {'body': 'comment'}
