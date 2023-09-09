"""This module holds models used in ecopost."""

import random
import string
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.shortcuts import reverse
from datetime import datetime
from cloudinary.models import CloudinaryField


STATUS = ((0, "投稿前"), (1, "投稿済み"))

COMMENT_STATUS = ((0, "オリジナル"), (1, "編集済み"), (2, "削除済み"))

CATEGORY = (('animals', '動物を守る'),
            ('aquatic systems', '海、川、湖を守る'),
            ('soil & trees', '土と木を守る'),
            ('save resources', 'その他資源を守る'),
            ('eco-conscious life style', '環境に配慮したライフスタイル'),
            ('others', 'その他'))


class Post(models.Model):
    """Hold fields of Post model and functions around them."""
    title = models.CharField(max_length=80)
    slug = models.SlugField(max_length=80, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="posts")
    featured_flag = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    published_on = models.DateTimeField(null=True, blank=True)
    content = models.TextField()
    featured_image = CloudinaryField('image',
                                     default='default',
                                     blank=True,
                                     transformation={
                                        'crop': 'fill_pad',
                                        'width': 510,
                                        'height': 340,
                                        'gravity': 'auto',
                                        'q_auto': 'good'
                                     })
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User,
                                   related_name='post_likes',
                                   blank=True)
    num_of_likes = models.IntegerField(default=0)
    city = models.CharField(max_length=25)
    category = models.CharField(max_length=30, choices=CATEGORY,
                                default='others')
    bookmark = models.ManyToManyField(User, related_name='bookmarked',
                                      blank=True)

    class Meta:
        ordering = ['-created_on', '-published_on']

    def save(self, *args, **kwargs):
        """
        Assign a slug if the post has no slug.
        If the status is 'Published,' but the published date
        is None, assign the current date and time.
        """
        if not self.slug:
            # add a random string after the title
            random_str = ''.join(random.choices(string.ascii_letters +
                                 string.digits, k=16))
            self.slug = slugify(self.title + '-' + random_str)
        # if the status is 2 ("Published") but published_on is None,
        # assign the current date & time.
        if self.status == 1 and not self.published_on:
            self.published_on = datetime.utcnow()
        # remove p tags in case the content contains them
        if self.content.startswith("<p>"):
            self.content = self.content[3:]
        if self.content.endswith("</p>"):
            self.content = self.content[:len(self.content)-4]
        # store num of likes if the post id exists.
        if self.id is not None:
            self.num_of_likes = self.likes.count()
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Return the title.
        :return: title
        :rtype: str
        """
        return self.title

    def status_value(self):
        """
        Return presentable values for status.
        :return: status descrption
        :rtype: str
        """
        if self.status == 0:
            return "未投稿"
        # if submited or published, return the status as it is.
        else:
            return "投稿中"

    def pub_date(self):
        """
        Return the published date.
        If the post hasn't been published, return 'Not published.'
        :returns: published_on or 'Not published'
        :rtype: str
        """
        if self.status == 1:
            return self.published_on.strftime("%m/%d, %Y")
        else:
            return '未投稿'

    def excerpt(self):
        """
        Return the first 200 letters of the post.
        :returns: excerpt
        :rtype: str
        """
        excerpt = str(self.content)[0:199] + "..."
        return excerpt

    def get_absolute_url(self):
        """
        Return the URL of 'Detail Page.'
        :return: reverse
        """
        return reverse('detail_page', kwargs={'slug': self.slug})


class Comment(models.Model):
    """Hold fields of Comment model and the functions around them."""
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    commenter = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name='commenter')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    comment_status = models.IntegerField(choices=COMMENT_STATUS, default=0)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        """
        Return the comment body and the commenter.
        :return: comment & the commenter
        :rtype: str
        """
        return f"{self.body} by {self.commenter.username}"
