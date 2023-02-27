from django.contrib import admin
from .models import Book, Author, BookCategory, BookOrder, Basket


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'description', 'rating', 'in_stock', 'slug')
    list_display_links = ('title',)
    search_fields = ('title', 'author')
    list_editable = ('in_stock',)
    list_filter = ('author',)
    # prepopulated_fields = {'slug': ('title',)}


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(BookCategory)
admin.site.register(BookOrder)
admin.site.register(Basket)
