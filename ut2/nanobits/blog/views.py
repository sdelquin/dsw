from django.shortcuts import redirect, render
from django.utils.text import slugify

from .forms import AddPostForm
from .models import Post


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


def add_post(request):
    if request.method == 'GET':
        form = AddPostForm()
    else:
        if (form := AddPostForm(data=request.POST)).is_valid():
            post = form.save(commit=False)
            post.slug = slugify(post.title)
            post.save()
            return redirect('blog:home')
    return render(request, 'blog/post/add.html', dict(form=form))
