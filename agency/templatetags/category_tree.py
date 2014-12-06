from django import template
from agency.models import Category

register = template.Library()

@register.inclusion_tag('agency/category_tree.html',takes_context=True)
def category_tree(context,category):
    children = Category.objects.filter(parent_category=category)
    return {'category': category, 'children' : children,}
