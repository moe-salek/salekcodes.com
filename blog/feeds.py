from django.contrib.syndication.views import Feed
from django.shortcuts import get_object_or_404
from django.urls import reverse

from blog.models import Tag
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


class TaggedEchoesFeed(EchoesFeed):
    def get_object(self, request, tag_name: str):
        return get_object_or_404(Tag, name=tag_name)

    def title(self, obj):
        return f'salekcodes.ir — Echoes tagged #{obj.name}'

    def link(self, obj):
        return reverse('echoes_by_tag', kwargs={'tag_name': obj.name})

    def description(self, obj):
        return f'Echoes tagged #{obj.name} from Moe Salek.'

    def items(self, obj):
        return published_posts().filter(tags=obj)[:FEED_SIZE]
