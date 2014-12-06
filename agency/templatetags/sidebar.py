from django import template
from agency.models import Category


register = template.Library()
@register.inclusion_tag("agency/sidebar.html")
def show_sidebar():
    category_list = Category.objects.filter(parent_category__isnull=True)
    context_dict = {'categories': category_list}
    return  context_dict
    
    
