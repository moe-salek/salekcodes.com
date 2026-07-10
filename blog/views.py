from django.shortcuts import get_object_or_404, redirect, render

from blog.models import Post

ECHOES_PAGE_SIZE = 10


def echoes(request):
    echo_posts = Post.objects.filter(status=Post.Status.PUBLISHED).order_by('-created_at')[:ECHOES_PAGE_SIZE]
    ctx = {'echo_post_list': echo_posts}
    return render(request, 'blog/echoes.html', ctx)


def echoes_archive(request):
    echo_posts = Post.objects.filter(status=Post.Status.PUBLISHED).order_by('-created_at')
    ctx = {'echo_post_list': echo_posts}
    return render(request, 'blog/echoes_archive.html', ctx)


def echo_unique_page(request, slug: str):
    post = get_object_or_404(Post, slug=slug, status=Post.Status.PUBLISHED)
    ctx = {'echo_post': post}
    return render(request, 'blog/echo_unique_page.html', ctx)


def echo_legacy_redirect(request, echo_id: int):
    post = get_object_or_404(Post, id=echo_id, status=Post.Status.PUBLISHED)
    return redirect('echo_unique_page', slug=post.slug, permanent=True)
