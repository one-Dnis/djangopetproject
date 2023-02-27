from django.forms import ModelForm
from .models import Book, Author, Basket, BookCategory, BookOrder


class BooksForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].empty_label = 'Автор'

    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'category', 'in_stock', 'photo', 'slug']


class AuthorsForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'info']


class BookCategoryForm(ModelForm):
    class Meta:
        model = BookCategory
        fields = ['name']


class BasketForm(ModelForm):
    class Meta:
        model = Basket
        fields = ['user', 'order', 'is_done']


class BookOrderForm(ModelForm):
    class Meta:
        model = BookOrder
        fields = ['quantity', 'book']
