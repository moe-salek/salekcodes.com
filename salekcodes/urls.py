from django.conf import settings
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

from blog.sitemaps import EchoSitemap
from core.sitemaps import StaticViewSitemap
from core.views import robots_txt

sitemaps = {'static': StaticViewSitemap, 'echoes': EchoSitemap}

urlpatterns = [
    # core:
    path('', include('core.urls')),
    # blog:
    path('echoes/', include('blog.urls')),
    # seo:
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('robots.txt', robots_txt, name='robots_txt'),
    # admin panel:
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
