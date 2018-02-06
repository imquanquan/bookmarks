from django import template

from ..models import Category, Tag

register = template.Library()

@register.simple_tag
def get_categories():
    return Category.objects.all()

@register.simple_tag
def get_tags():
    tag_list =  list(Tag.objects.all())
    tag_id = [str(i) for i in range(1, len(tag_list) + 1)]
    return zip(tag_id, tag_list)
    
@register.assignment_tag
def get_book_tags(book):
    book_obj = Tag.objects.get(name=book)
    tag_list = list(book_obj.Tag.all())
    tag_str = ' '.join(tag_list)
    return tag_str