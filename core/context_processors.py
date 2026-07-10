from django.conf import settings


def site(request):
    return {'site_url': settings.SITE_URL}
