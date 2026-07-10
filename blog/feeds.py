from django.contrib.syndication.views import Feed

from blog.templatetags.markdown_utils import markdown_to_html
from blog.views import published_posts

FEED_SIZE = 20


class EchoesFeed(Feed):
    title = 'salekcodes.ir — Echoes'
    link = '/echoes/'
    description = 'Short notes from Moe Salek on building, breaking, and learning.'

    def items(self):
        return published_posts()[:FEED_SIZE]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return markdown_to_html(item.content)

    def item_pubdate(self, item):
        return item.published_at

    def item_categories(self, item):
        return [tag.name for tag in item.tags.all()]
