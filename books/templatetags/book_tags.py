from ..models import Book
from django import template

register = template.Library()


@register.simple_tag(name='books_from_tags')
def get_books():
    return Book.objects.all()
