from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.html import strip_tags
from django.utils.text import Truncator

from blog.models import Post, Tag
from blog.templatetags.markdown_utils import markdown_to_html

ECHOES_PAGE_SIZE = 10
ARCHIVE_PAGE_SIZE = 20


def published_posts():
    return Post.objects.filter(status=Post.Status.PUBLISHED).prefetch_related('tags').order_by('-published_at')


def echoes(request):
    ctx = {'echo_post_list': published_posts()[:ECHOES_PAGE_SIZE]}
    return render(request, 'blog/echoes.html', ctx)


def echoes_archive(request):
    paginator = Paginator(published_posts(), ARCHIVE_PAGE_SIZE)
    page = paginator.get_page(request.GET.get('page'))
    ctx = {'echo_post_list': page.object_list, 'page': page}
    return render(request, 'blog/echoes_archive.html', ctx)


def echoes_by_tag(request, tag_name: str):
    tag = get_object_or_404(Tag, name=tag_name)
    paginator = Paginator(published_posts().filter(tags=tag), ARCHIVE_PAGE_SIZE)
    page = paginator.get_page(request.GET.get('page'))
    ctx = {'echo_post_list': page.object_list, 'page': page, 'tag': tag}
    return render(request, 'blog/echoes_by_tag.html', ctx)


def echoes_search(request):
    query = request.GET.get('q', '').strip()
    if query:
        results = published_posts().filter(Q(title__icontains=query) | Q(content__icontains=query))
    else:
        results = Post.objects.none()
    paginator = Paginator(results, ARCHIVE_PAGE_SIZE)
    page = paginator.get_page(request.GET.get('page'))
    ctx = {'echo_post_list': page.object_list, 'page': page, 'query': query}
    return render(request, 'blog/echoes_search.html', ctx)


def echo_unique_page(request, slug: str):
    post = get_object_or_404(Post, slug=slug, status=Post.Status.PUBLISHED)
    meta_description = Truncator(strip_tags(markdown_to_html(post.content))).chars(160)
    ctx = {'echo_post': post, 'meta_description': meta_description}
    return render(request, 'blog/echo_unique_page.html', ctx)


def echo_legacy_redirect(request, echo_id: int):
    post = get_object_or_404(Post, id=echo_id, status=Post.Status.PUBLISHED)
    return redirect('echo_unique_page', slug=post.slug, permanent=True)
