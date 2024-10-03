from django.shortcuts import render

from blog.models import Post


def home(request):
    num_posts = Post.objects.count()
    posts = Post.objects.all()
    return render(
        request,
        'blog/home.html',
        {'num_posts': num_posts, 'posts': posts},
    )


def post_detail(request, post_slug: str):
    post = Post.objects.get(slug=post_slug)
    return render(request, 'blog/posts/detail.html', dict(post=post))
