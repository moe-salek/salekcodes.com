from django.contrib.sitemaps import Sitemap

from blog.models import Post


class EchoSitemap(Sitemap):
    protocol = 'https'
    changefreq = 'monthly'
    priority = 0.6

    def items(self):
        return Post.objects.filter(status=Post.Status.PUBLISHED).order_by('-published_at')

    def lastmod(self, obj):
        return obj.modified_at
