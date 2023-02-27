from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.SET_DEFAULT, default='автор не выбран')
    description = models.TextField()
    category = models.ManyToManyField('BookCategory', default='категория не выбрана')
    rating = models.DecimalField(max_digits=4, decimal_places=1, default=0)
    # in_stock = models.IntegerField(default=0)
    in_stock = models.PositiveSmallIntegerField(default=0)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL')
    photo = models.ImageField(upload_to='photos/', default='photos/no_picture_for_book.png')

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book', kwargs={'books_slug': self.slug})


class Author(models.Model):
    name = models.CharField(max_length=50)
    info = models.TextField(default='добавьте биографию')

    def __str__(self):
        return self.name


class BookCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ManyToManyField('BookOrder')
    is_done = models.BooleanField(default=False)
    order_datatime = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'

    def __str__(self):
        return self.user, self.order

    # def get_absolute_url(self):
    #     return reverse('add-book', kwargs={'books_slug': self.slug})


class BookOrder(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
