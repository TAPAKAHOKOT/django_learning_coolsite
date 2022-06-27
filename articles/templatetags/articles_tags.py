from django import template
from articles.models import *

register = template.Library()


@register.simple_tag()
def get_all_categories():
    return Categories.objects.all()


@register.simple_tag()
def get_published_categories():
    return get_all_categories().filter(is_published=True).order_by('-priority', 'name')


@register.simple_tag()
def get_published_ordered_categories():
    return get_published_categories().order_by('-priority', 'name')
