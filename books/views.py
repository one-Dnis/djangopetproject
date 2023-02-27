from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import UpdateView, DetailView
from .models import Book, Author
from .forms import BooksForm, AuthorsForm, BookCategoryForm, Basket, BookOrder
from .utils import Tools


# Create your views here.
def index(request):
    return render(request, 'books/index.html')


def book_details(request, books_slug):
    book = get_object_or_404(Book, slug=books_slug)
    return render(request, 'books/book-details.html', {'book': book})

# class BookView(DetailView):
#     model = Book
#     template_name = 'books/book-details.html'
#     context_object_name = 'book'


def add_book(request):
    if request.method == 'POST':
        form = BooksForm(request.POST, request.FILES)

        if form.is_valid():
            # slug = Tools.create_slug(form.cleaned_data.get('title'))
            # form.cleaned_data = form.cleaned_data.update({'slug': slug})
            # print(form.cleaned_data)
            form.save()
            return redirect('index')
    else:
        form = BooksForm()
    return render(request, 'books/add-book.html', {'form': form})


class UpdateBook(UpdateView):
    model = Book
    form_class = BooksForm
    template_name = 'books/add-book.html'
    context_object_name = 'book'




    # model = Book
    # form_class = BooksForm()
    # template_name = 'books/add-book.html'
    # fields = ['title', 'author', 'description', 'category', 'in_stock', 'photo', 'slug']


def add_author(request):
    if request.method == 'POST':
        form = AuthorsForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('add-book')
    else:
        form = AuthorsForm()
    return render(request, 'books/add-author.html', {'form': form})


def add_category(request):
    if request.method == 'POST':
        form = BookCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add-book')
    else:
        form = BookCategoryForm()
    return render(request, 'books/add-category.html', {'form': form})


def add_book_to_basket(request, books_slug):
    # book_id = Book.objects.values('id').get(slug=books_slug)
    book = Book.objects.get(slug=books_slug)
    user = User.objects.get(username=request.user.username)
    print(book, user)
    # print(f'вы пытаететсь купить книгу {get_object_or_404(Book, id=book_id.get("id"))} {request.user.username}')
    order = BookOrder.objects.create(book=book, quantity=1)
    order.save()
    # order = BookOrder.objects.get(book=book)
    basket = Basket.objects.create(user=user, order=BookOrder.objects.get(book=book))
    basket.save()

    return redirect('index')


def delete_book(request, books_slug):
    Book.objects.get(slug=books_slug).delete()
    return redirect('index')
