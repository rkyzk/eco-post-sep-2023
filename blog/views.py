"""This module holds view functions for ecopost."""

from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.db.models import Q
from datetime import datetime, timedelta
from django.core.exceptions import PermissionDenied
from .filters import PostFilter
from .forms import PostForm, CommentForm
from .models import Post, Comment, CATEGORY
from django.http import JsonResponse
from django.core.paginator import Paginator


#　指定する数以上の「いいね」を集めた記事が「人気の記事」に表示される。
min_num_likes = 5


def handler500(request):
    """500 エラーページを表示"""
    return render(
        request,
        '500.html',
        {}
    )


class PostList(generic.ListView):
    """おすすめ記事を取得、ホームページを表示"""
    model = Post
    queryset = Post.objects.filter(featured_flag=True).order_by(
            "-created_on")[:3]
    template_name = "blog/index.html"


class AddPost(LoginRequiredMixin, generic.CreateView):
    """
    記事投稿のページを表示
    """
    model = Post
    template_name = "blog/add_post.html"
    form_class = PostForm

    def form_valid(self, form):
        """
        入力内容をバリデート
        arguments: self, form: Post form
        :rtype: method
        """
        # ユーザーを投稿者に設定
        form.instance.author = self.request.user
        message = '記事を下書きとして保存しました。'
        # 投稿ボタンがクリックされたならばステータスを１（投稿済み）に設定
        if 'publish' in self.request.POST.keys():
            form.instance.status = 1
            message = "記事が投稿されました。"
        form.save()
        messages.add_message(self.request, messages.SUCCESS, message)
        return super(AddPost, self).form_valid(form)


class PostDetail(View):
    """
    全記事内容、コメント、コメント入力フォームを表示
    """
    def get(self, request, slug, *args, **kwargs):
        """
        記事詳細を取得、表示
        argument: self, request, slug
        :rtype: method
        """
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.order_by('created_on')
        # ユーザーが「いいね」していたら 'liked' をTrueに設定
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        # ユーザーがブックマークしていたら 'bookmarked' をTrueに設定
        bookmarked = False
        if post.bookmark.filter(id=self.request.user.id).exists():
            bookmarked = True
        return render(
            request,
            "blog/post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "bookmarked": bookmarked,
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        入力されたコメントをバリデート後、コメントを保存して表示。
        エラーの際は空のコメントフォームとエラーメッセージを表示。
        arguments: self, request, slug, *args, **kwargs
        :rtype: method
        """
        post = Post.objects.filter(slug=slug)[0]
        comments = post.comments.order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        bookmarked = False
        if post.bookmark.filter(id=self.request.user.id).exists():
            bookmarked = True
        # 入力内容をコメントフォームに設定
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # 投稿者をユーザーに設定
            comment_form.instance.commenter = request.user
            comment = comment_form.save(commit=False)
            # コメントがどの記事に属するのか設定
            comment.post = post
            comment.save()
            messages.add_message(request, messages.SUCCESS,
                                 'コメントが投稿されました。')
        else:
            # エラーの場合、空コメントフォームとメッセージを表示
            comment_form = CommentForm()
            messages.add_message(request, messages.INFO, "エラー発生。" +
                                 "コメントは保存されませんでした。")
        return render(
            request,
            "blog/post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "bookmarked": bookmarked,
                "comment_form": CommentForm()
            },
        )


def postLike(request, slug):
    """ポストモデルの属性「likes」にユーザを追加または削除"""
    if request.is_ajax and request.method == 'POST':
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        post.save()
        response = {
            'message': 'done'
        }
        return JsonResponse(response)


def bookmark(request, slug):
    """ユーザが「bookmark」に存在していたら削除、存在していなかったら追加。"""
    if request.is_ajax and request.method == 'POST':
        post = get_object_or_404(Post, slug=slug)
        if post.bookmark.filter(id=request.user.id).exists():
            post.bookmark.remove(request.user)
        else:
            post.bookmark.add(request.user)
        post.save()
        response = {
            'message': 'done'
        }
        return JsonResponse(response)


class UpdatePost(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    """記事を更新"""
    model = Post
    template_name = "blog/update_post.html"
    form_class = PostForm

    def form_valid(self, form):
        """
        入力内容をバリデート、
        arguments: self, form
        :return: super()
        :rtype: method
        """
        form.instance.author = self.request.user
        message = '記事が更新されました。'
        # 投稿ボタンが押されたら、ポストのステータスを「1」に変更 
        if 'publish' in self.request.POST.keys():
            form.instance.status = 1
            message = "記事が投稿されました。"
        form.save()
        messages.add_message(self.request, messages.SUCCESS, message)
        return super(UpdatePost, self).form_valid(form)

    def test_func(self):
        """
        ユーザーが記事投稿者だったらTrueを返す。
        :return: True/False
        :rtype: boolean
        """
        slug = self.kwargs.get('slug')
        post = get_object_or_404(Post, slug=slug)
        return post.author == self.request.user


class DeletePost(LoginRequiredMixin, View):
    """記事を削除"""

    def post(self, request, slug, *args, **kwargs):
        """
        記事を削除しホームにリダイレクト
        arguments: self, request, slug, *args. **kwargs
        :returns: HttpResponseRedirect()
        :rtype: method
        """
        post = get_object_or_404(Post, slug=slug)
        # ユーザーが記事投稿者だったら記事を削除
        if post.author == self.request.user:
            post.delete()
            message = '記事が削除されました。'
            messages.add_message(request, messages.SUCCESS, message)
            return HttpResponseRedirect(reverse('home'))
        else:
            raise PermissionDenied()


def getComment(request, slug):
    """コメント更新フォームに表示するためコメントを取得"""
    if request.is_ajax and request.method == 'GET':
        id = request.GET['id']
        comment = get_object_or_404(Comment, id=id)
        # ユーザーチェック
        response = {
            'content': comment.body
        }
        return JsonResponse(response)
        

def updateComment(request, slug):
    """更新されたコメントをDBに保存"""
    if request.is_ajax and request.method == 'POST':
        id = request.POST['id']
        comment = get_object_or_404(Comment, id=id)
        updatedCmmt = request.POST['comment']
        comment.comment_status = 1
        comment.body = updatedCmmt
        comment.save()
        response = {
            'message': 'Comment updated'
        }
        return JsonResponse(response)

class DeleteComment(LoginRequiredMixin, UserPassesTestMixin, View):

    def post(self, request, id, *args, **kwargs):
        """
        コメントステータスを「2, Deleted」に変更
        arguments: id: comment id
        :rtype: method
        """
        comment = get_object_or_404(Comment, id=id)
        comment.comment_status = 2
        comment.save()
        slug = comment.post.slug
        message = 'コメントが削除されました。'
        messages.add_message(request, messages.SUCCESS, message)
        return HttpResponseRedirect(reverse('detail_page', args=[slug]))

    def test_func(self):
        """
        ユーザーがコメント投稿者ならばTrueを返す。
        :rtype: boolean
        """
        id = self.kwargs.get('id')
        comment = get_object_or_404(Comment, id=id)
        return comment.commenter == self.request.user


class MyPage(LoginRequiredMixin, UserPassesTestMixin, View):

    def get(self, request, pk, *args, **kwargs):
        """
        1) 自分で書いた記事
        2) コメントした記事
        3) ブックマークした記事
        を取得、表示。
        arguments: self, request, pk: pk of the user, *args, **kwargs
        :rtype: method
        """
        my_posts = Post.objects.filter(author=pk)
        # コメントした記事を取得
        comments = Comment.objects.filter(commenter__id=pk,
                                          comment_status__in=[0, 1])
        commented_posts = [comment.post for comment in comments]
        # 重複削除
        commented_posts = list(dict.fromkeys(commented_posts))
        # ブックマークした記事を取得
        bookmarked_posts = Post.objects.filter(bookmark__in=[request.user.id])
        return render(
            request,
            "blog/my_page.html",
            {
                "my_posts": my_posts,
                "commented_posts": commented_posts,
                "bookmarked_posts": bookmarked_posts
            },
        )

    def test_func(self):
        """
        アクセスしようとしているマイページのIDが
        ログインしているユーザのIDであればTrueを返す。
        :rtype: boolean
        """
        return self.kwargs.get('pk') == self.request.user.pk


class SearchPosts(View):
    """検索ページを表示、入植内容をもとに検索、結果を表示。"""

    def get(self, request, *args, **kwargs):
        """
        検索ページを表示、検索実行、結果をテンプレートに送る
        arguments: self, request, *args, **kwargs
        :returns: render()
        :rtype: method
        """
        # カテゴリーを取得
        category_choices = Post._meta.get_field('category').choices
        # カテゴリーTupleの２個目の項目を取得
        categories = [cat[1] for cat in category_choices]
        posts = []
        search = False
        no_input = False
        postFilterForm = PostFilter()
        if 'search' in request.GET.keys():
            search = True
            input = request.GET['title'].strip() + request.GET['author__username'].strip() + \
                    request.GET['keyword'].strip() + \
                    request.GET['city'].strip() + \
                    request.GET['published_after'].strip() + \
                    request.GET['published_before'].strip()

            if (input == "" and
                (request.GET['category'] == "Choose..." or request.GET['category'] == "") and
                (request.GET['num_of_likes'] == "0" or request.GET['num_of_likes'] == "")):
                    no_input = True
            else:
                posts = Post.objects.filter(status=1).order_by('-published_on')
                postFilterForm = PostFilter(request.GET, queryset=posts)
                posts = postFilterForm.qs
        context = {
            'categories': categories,
            'posts': posts,
            'postForm': postFilterForm,
            'search': search,
            'no_input': no_input,
        }
        return render(request, "blog/search_posts.html", context)


class RecentPosts(generic.ListView):
    """
    過去7日に投稿された記事を取得
    「今週の記事」ページを表示
    """
    model = Post
    template_name = "blog/paginated_posts_list.html"
    paginate_by = 6
    # 過去7日に投稿された記事を取得
    filterargs = {
            'status': 1,
            'published_on__date__gte': datetime.utcnow() - timedelta(days=7),
            'featured_flag': False
            }
    queryset = Post.objects.filter(**filterargs).order_by("-published_on")

    def get_context_data(self, **kwargs):
        """
        コンテキストにページタイトルをセット
        :return: context
        :rtype: object
        """
        context = super().get_context_data(**kwargs)
        context["page_title"] = "今週の記事"
        return context


class PopularPosts(generic.ListView):
    """
    いいねの回数が指定以上の記事を取得、
    「人気の記事」ページに表示
    """
    model = Post
    template_name = "blog/paginated_posts_list.html"
    paginate_by = 6
    # １８行目で指定されたmin_num_likes以上の回数「いいね」された記事を取得
    queryset = Post.objects.filter(
            status=1,
            featured_flag=False,
            num_of_likes__gte=min_num_likes
        ).order_by("-published_on")

    def get_context_data(self, **kwargs):
        """
        コンテキストにページタイトルを設定
        :return: context
        :rtype: object
        """
        context = super().get_context_data(**kwargs)
        context["page_title"] = "人気の記事"
        return context
