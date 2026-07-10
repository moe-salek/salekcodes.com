from django.shortcuts import render

from core.models import Social


def coming_soon(request):
    return render(request, 'core/coming_soon.html', {})


def index(request):
    return render(request, 'core/index.html', {})


def about(request):
    return render(request, 'core/about.html', {})


def connect(request):
    social = Social.objects.first() or Social()
    return render(request, 'core/connect.html', {'social': social})
