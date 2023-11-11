"""filters.pyのテスト"""

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment
from .filters import PostFilter


class TestViews(TestCase):

    def setUp(self):
        """ユーザーと記事を作成"""
        self.user1 = User.objects.create_user(username="user1")
        self.user2 = User.objects.create_user(username="user2")
        self.post1 = Post.objects.create(title='title 1',
                                         author=self.user1,
                                         content='abc',
                                         city='test',
                                         status=1,
                                         featured_flag=True,
                                         category='others')
        self.post2 = Post.objects.create(title='title 2',
                                         author=self.user1,
                                         content='abc',
                                         city='test',
                                         status=1,
                                         featured_flag=True,
                                         category='others')
        self.post3 = Post.objects.create(title='title 3',
                                         author=self.user1,
                                         content='abc',
                                         city='test',
                                         status=1,
                                         featured_flag=True,
                                         category='others')
        self.post4 = Post.objects.create(title='test 1',
                                         author=self.user1,
                                         content='def',
                                         city='city',
                                         status=1,
                                         category='others')
        self.post5 = Post.objects.create(title='test 2',
                                         author=self.user1,
                                         content='def',
                                         city='city',
                                         status=1,
                                         category='others')
        self.post6 = Post.objects.create(title='test 3',
                                         author=self.user1,
                                         content='def',
                                         city='city',
                                         status=0,
                                         category='others')

    def test_filter_keyword_filters_right_posts(self):
        pass