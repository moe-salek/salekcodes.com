from django.shortcuts import render


def echoes(request):
    return render(request, 'blog/echoes.html', {})
