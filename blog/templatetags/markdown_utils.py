import markdown
import nh3
from django import template

register = template.Library()

# nh3 defaults plus the class attribute, which codehilite needs for syntax colors
ALLOWED_ATTRIBUTES = {**nh3.ALLOWED_ATTRIBUTES, '*': nh3.ALLOWED_ATTRIBUTES.get('*', set()) | {'class'}}


@register.filter
def markdown_to_html(text: str):
    html = markdown.markdown(text, extensions=['fenced_code', 'codehilite'])
    return nh3.clean(html, attributes=ALLOWED_ATTRIBUTES)
