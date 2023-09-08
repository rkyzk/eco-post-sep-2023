"""This module holds tests for forms."""

from django.test import TestCase
from django.contrib.auth.models import User
from .forms import PostForm, CommentForm
from .models import Post, Comment


class TestPostForm(TestCase):
    """Tests Post form."""

    def setUp(self):
        """create a test user"""
        self.user_1 = User.objects.create(username="test1",
                                          password="password")

    def test_post_title_is_required(self):
        form = PostForm({
            'title': '',
            'author': self.user_1,
            'content': 'content',
            'city': 'test',
            'country': 'IR',
            'category': 'others'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_post_content_is_required(self):
        form = PostForm({
            'title': 'title_3',
            'author': self.user_1,
            'content': '',
            'city': 'test',
            'country': 'IR',
            'category': 'others'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['content'][0],
                         'This field is required.')

    def test_post_featured_image_is_not_required(self):
        form = PostForm({
            'title': 'title_3',
            'author': self.user_1,
            'content': 'content',
            'city': 'test',
            'country': 'IR',
            'category': 'others'
        })
        self.assertTrue(form.is_valid())

    def test_post_category_is_required(self):
        form = PostForm({
            'title': 'title_3',
            'author': self.user_1,
            'content': 'content',
            'city': 'test',
            'country': 'IR',
            'category': ''
        })
        self.assertFalse(form.is_valid())
        self.assertIn('category', form.errors.keys())
        self.assertEqual(form.errors['category'][0],
                         'This field is required.')

    def test_post_city_is_required(self):
        form = PostForm({
            'title': 'title_3',
            'author': self.user_1,
            'content': 'content',
            'city': '',
            'country': 'IR',
            'category': 'others'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('city', form.errors.keys())
        self.assertEqual(form.errors['city'][0],
                         'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = PostForm()
        self.assertEqual(
            form.Meta.fields,
            ['title', 'content', 'featured_image',
             'city', 'category']
        )


class TestCommentForm(TestCase):
    """Tests comment form"""

    def setUp(self):
        """create test user"""
        self.user_1 = User.objects.create(username="test1",
                                          password="password")

    def test_comment_body_is_required(self):
        form = CommentForm({
            'body': '',
            'author': self.user_1,
        })
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = CommentForm()
        self.assertEqual(
            form.Meta.fields,
            ('body',)
        )


if __name__ == "__main__":
    main()
