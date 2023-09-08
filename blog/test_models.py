"""This module holds tests for models."""

from django.test import TestCase
from django.contrib.auth.models import User
from datetime import datetime
from sqlite3 import IntegrityError
from .models import Post, Comment


class TestPostModel(TestCase):

    def setUp(self):
        """create test users and posts"""
        self.user1 = User.objects.create(username="test1", password="password")
        self.user2 = User.objects.create(username="test2", password="password")
        self.post1 = Post.objects.create(
            title="title1",
            author=self.user1,
            content="test sentences"
            )
        self.post2 = Post.objects.create(
            title="title2",
            author=self.user2,
            content="test 2 sentences"
            )

    def test_featured_flag_default_to_False(self):
        self.assertEqual(self.post1.featured_flag, False)

    def test_featured_image_default_to_default(self):
        self.assertEqual(self.post1.featured_image, 'default')

    def test_category_default_to_others(self):
        self.assertEqual(self.post1.category, 'others')

    def test_status_default_to_0(self):
        self.assertEqual(self.post1.status, 0)

    def test_posts_ordered_by_created_on_newest_to_oldest(self):
        posts = Post.objects.all()
        i = 0
        for i in range(len(posts) - 2):
            self.assertGreater(posts[i].created_on, posts[i+1].created_on)
            i += 1

    def test_post_will_be_slugified(self):
        self.assertTrue(self.post1.slug.startswith('title1'))

    def test_str_method_will_return_title(self):
        self.assertEqual(str(self.post1), 'title1')

    def test_num_of_likes_count_num_of_likes(self):
        self.post1.likes.add(self.user2)
        self.post1.save()
        self.assertEqual(self.post1.num_of_likes,
                         self.post1.likes.count())

    def test_status_value_returns_saved_as_draft_if_status_0(self):
        self.assertEqual(self.post1.status_value(), 'Saved as draft')

    def test_status_value_returns_published_if_status_1(self):
        self.post1.status = 1
        self.assertEqual(self.post1.status_value(), 'Published')

    def test_pub_date_returns_string_message_if_not_published(self):
        self.assertEqual(self.post1.pub_date(), 'Not published')

    def test_pub_date_returns_specified_format_if_published(self):
        date = datetime.utcnow()
        self.post1.status = 1
        self.post1.published_on = date
        self.assertEqual(self.post1.pub_date(), date.strftime("%b %d, %Y"))

    def test_excerpt_returns_specified_str(self):
        content = "I'm writing a long content to test " + \
            "if the excerpt method returns the first 199 characters and " + \
            "... are returned. test test test test test sentences." + \
            "test sentences, test sentences, test sentences "
        post3 = Post.objects.create(
            title="title3",
            author=self.user1,
            content=content
        )
        self.assertEqual(post3.excerpt(), str(content)[0:199] + "...")

    def test_get_absolute_url(self):
        self.assertEqual(self.post1.get_absolute_url(),
                         '/detail/' + self.post1.slug + '/')


class TestCommentModels(TestCase):

    def setUp(self):
        """create test users and posts"""
        self.user1 = User.objects.create(username="test1", password="password")
        self.user2 = User.objects.create(username="test2", password="password")
        self.post1 = Post.objects.create(
            title="title1",
            author=self.user1,
            content="test sentences"
            )
        self.comment1 = Comment.objects.create(
            commenter=self.user1,
            post=self.post1,
            body='test comment'
        )

    def test_comment_status_default_to_0(self):
        self.assertEqual(self.comment1.comment_status, 0)

    def test_comments_ordered_from_oldest_to_newest(self):
        comment2 = Comment.objects.create(
            commenter=self.user1,
            post=self.post1,
            body='2nd test comment'
        )
        comments = Comment.objects.all()
        i = 0
        for i in range(len(comments) - 2):
            self.assertLess(comments[i].created_on, comments[i+1].created_on)
            i += 1

    def test_str_method_will_return_body_and_commenter(self):
        self.assertEqual(str(self.comment1), 'test comment by test1')


if __name__ == "__main__":
    main()
