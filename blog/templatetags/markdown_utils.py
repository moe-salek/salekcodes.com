import markdown
from django import template

register = template.Library()


@register.filter
def markdown_to_html(text: str):
    return markdown.markdown(text, extensions=['fenced_code', 'codehilite'])
