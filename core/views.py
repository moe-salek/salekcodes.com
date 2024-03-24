from django.shortcuts import render


def coming_soon(request):
    return render(request, 'core/coming_soon.html', {})


def index(request):
    return render(request, 'core/index.html', {})


def about(request):
    return render(request, 'core/about.html', {})


def contact(request):
    return render(request, 'core/contact.html', {})
