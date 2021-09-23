from django import template
from ..models import Category

register = template.Library()


@register.simple_tag(name='get_list_categories')
def get_categories():
        return  Category.objects.all()

@register.inclusion_tag('blog/list_categories.html')
def show_categories(arg1= 'Hello', arg2='World'):
    categies = Category.objects.all()
    return {
        "categories": categies,
        "arg1": arg1,
        "arf2": arg2,
    }