"""This module holds url paths used in blog app."""

from . import views
from django.urls import path


urlpatterns = [
  path('', views.PostList.as_view(), name='home'),
  path('add_story/', views.AddPost.as_view(), name='add_story'),
  path('recent_posts/', views.RecentPosts.as_view(), name='recent_posts'),
  path('popular_posts/', views.PopularPosts.as_view(),
       name='popular_posts'),
  path('search/', views.SearchPosts.as_view(), name='search'),
  path('my_page/<int:pk>/', views.MyPage.as_view(), name='my_page'),
  path('update/<slug:slug>/', views.UpdatePost.as_view(),
       name='update_post'),
  path('delete/<slug:slug>/', views.DeletePost.as_view(),
       name='delete_post'),
  path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
  path('bookmark/<slug:slug>/', views.Bookmark.as_view(),
       name='bookmark'),
  path('detail/<slug:slug>/get_comment/',
       views.getComment, name='get_comment'),
  path('delete_comment/comment<int:id>/', views.DeleteComment.as_view(),
       name='delete_comment'),
  path('detail/<slug:slug>/', views.PostDetail.as_view(), name='detail_page')
]
