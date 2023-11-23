"""本アプリで使用される記事とコメントモデル"""

import random
import string
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.shortcuts import reverse
from datetime import datetime
from cloudinary.models import CloudinaryField


# 記事のステータス
STATUS = ((0, "投稿前"), (1, "投稿済み"))

# コメントのステータス
COMMENT_STATUS = ((0, "オリジナル"), (1, "編集済み"), (2, "削除済み"))

# カテゴリー
CATEGORY = (('animals', '動物を守る'),
            ('aquatic systems', '海、川、湖を守る'),
            ('soil & trees', '土と木を守る'),
            ('save resources', 'その他資源を守る'),
            ('eco-conscious life style', '環境に配慮したライフスタイル'),
            ('others', 'その他'))


class Post(models.Model):
    """記事のモデル"""
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
        スラッグがない場合、スラッグを付与
        ステータスが「投稿済み」で投稿日が「None」の場合、
        投稿日をその時に日時に設定
        """
        if not self.slug:
            # タイトルにランダムな文字列を追加
            random_str = ''.join(random.choices(string.ascii_letters +
                                 string.digits, k=16))
            self.slug = slugify(self.title + '-' + random_str)
        # 投稿日がない場合、設定
        if self.status == 1 and not self.published_on:
            self.published_on = datetime.utcnow()
        # 記事にpタグがついていたら削除
        if self.content.startswith("<p>"):
            self.content = self.content[3:]
        if self.content.endswith("</p>"):
            self.content = self.content[:len(self.content)-4]
        # 記事にIDが設定されていたら、「いいね」の数を設定
        if self.id is not None:
            self.num_of_likes = self.likes.count()
        super().save(*args, **kwargs)

    def __str__(self):
        """
        タイトルを返す
        :return: title
        :rtype: str
        """
        return self.title

    def excerpt(self):
        """
        記事の最初の150文字を返す
        :returns: excerpt
        :rtype: str
        """
        excerpt = str(self.content)[0:79] + "..."
        return excerpt

    def get_absolute_url(self):
        """
        post_detailページのURLを返す
        :return: reverse
        """
        return reverse('detail_page', kwargs={'slug': self.slug})


class Comment(models.Model):
    """コメントモデル"""
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
        コメント内容と投稿者の名前を返す
        :return: comment & the commenter
        :rtype: str
        """
        return f"{self.body} by {self.commenter.username}"
