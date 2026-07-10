from django.shortcuts import render

from blog.views import published_posts
from core.models import Social

INDEX_ECHOES_COUNT = 5


def coming_soon(request):
    return render(request, 'core/coming_soon.html', {})


def index(request):
    ctx = {'echo_post_list': published_posts()[:INDEX_ECHOES_COUNT]}
    return render(request, 'core/index.html', ctx)


def about(request):
    return render(request, 'core/about.html', {})


def connect(request):
    social = Social.objects.first() or Social()
    return render(request, 'core/connect.html', {'social': social})
