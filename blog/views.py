from django.shortcuts import get_object_or_404, redirect, render
from django.utils.html import strip_tags
from django.utils.text import Truncator

from blog.models import Post
from blog.templatetags.markdown_utils import markdown_to_html

ECHOES_PAGE_SIZE = 10


def published_posts():
    return Post.objects.filter(status=Post.Status.PUBLISHED).prefetch_related('tags').order_by('-published_at')


def echoes(request):
    ctx = {'echo_post_list': published_posts()[:ECHOES_PAGE_SIZE]}
    return render(request, 'blog/echoes.html', ctx)


def echoes_archive(request):
    ctx = {'echo_post_list': published_posts()}
    return render(request, 'blog/echoes_archive.html', ctx)


def echo_unique_page(request, slug: str):
    post = get_object_or_404(Post, slug=slug, status=Post.Status.PUBLISHED)
    meta_description = Truncator(strip_tags(markdown_to_html(post.content))).chars(160)
    ctx = {'echo_post': post, 'meta_description': meta_description}
    return render(request, 'blog/echo_unique_page.html', ctx)


def echo_legacy_redirect(request, echo_id: int):
    post = get_object_or_404(Post, id=echo_id, status=Post.Status.PUBLISHED)
    return redirect('echo_unique_page', slug=post.slug, permanent=True)
