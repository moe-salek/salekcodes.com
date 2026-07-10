from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    protocol = 'https'
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return ['index', 'echoes', 'echoes_archive', 'about', 'connect']

    def location(self, item):
        return reverse(item)
