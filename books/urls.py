from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/<slug:books_slug>/', views.book_details, name='book'),
    # path('books/<slug:slug>/', views.BookView.as_view(), name='book'),
    path('add-book', views.add_book, name='add-book'),
    path('add-author', views.add_author, name='add-author'),
    path('add-category', views.add_category, name='add-category'),
    path('add-book-to-basket/<slug:books_slug>/', views.add_book_to_basket, name='add-book-to-basket'),
    path('delete-book/<slug:books_slug>/', views.delete_book, name='delete-book'),
    path('<slug:slug>/update/', views.UpdateBook.as_view(), name='update-book')
]
