from django.shortcuts import render
from django.http import HttpResponseNotFound

from blog.models import Post


def echoes(request):
    limit = 10
    echo_posts = Post.objects.filter(status=Post.Status.PUBLISHED).order_by('-created_at')[:limit].all()
    ctx = {'echo_post_list': echo_posts}
    return render(request, 'blog/echoes.html', ctx)


def echo_unique_page(request, echo_id: str):
    try:
        post = Post.objects.get(id=echo_id)
    except Post.DoesNotExist:
        return HttpResponseNotFound('404 - not found')

    if post.status != Post.Status.PUBLISHED:
        return HttpResponseNotFound('404 - not found')

    ctx = {'echo_post': post}

    return render(request, 'blog/echo_unique_page.html', ctx)
