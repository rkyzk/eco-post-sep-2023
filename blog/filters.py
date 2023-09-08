import django_filters
from .models import Post, CATEGORY
from django.forms.widgets import Input
from django.db.models import Q
from datetime import datetime


class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains',
                                      label="title")
    author__username = django_filters.CharFilter(lookup_expr='icontains',
                                                 label='author')
    published_after = django_filters.DateFilter(method='filter_start_date',
                                                label='from',
                                                widget=Input(
                                                    attrs={'type': 'date'}))
    published_before = django_filters.DateFilter(method='filter_end_date',
                                                 label='until',
                                                 widget=Input(
                                                    attrs={'type': 'date'}))
    num_of_likes = django_filters.NumberFilter(method='filter_likes',
                                               label='liked more than',
                                               widget=Input(
                                                    attrs={'min': int(0),
                                                           'type': 'number'}))
    category = django_filters.ChoiceFilter(choices=CATEGORY,
                                           empty_label='Choose...')
    city = django_filters.CharFilter(lookup_expr='icontains')
    keyword = django_filters.CharFilter(method='filter_keyword',
                                               label='keyword')

    class Meta:
        model = Post
        fields = ['title', 'author__username', 'content', 'published_on',
                  'num_of_likes', 'category', 'city']

    def filter_keyword(self, queryset, name, value):
        return queryset.filter(Q(title__icontains=value) |
                               Q(content__icontains=value))

    def filter_likes(self, queryset, name, value):
        return queryset.filter(Q(num_of_likes__gte=value))

    def filter_start_date(self, queryset, name, value):
        return queryset.filter(Q(published_on__gte=value))

    def filter_end_date(self, queryset, name, value):
        end_date = datetime.combine(value, datetime.max.time())
        return queryset.filter(Q(published_on__lte=end_date))
