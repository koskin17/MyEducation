from django.contrib import admin
from authentication.models import CustomUser
from author.models import Author
from book.models import Book
from order.models import Order
from django.contrib.admin import RelatedOnlyFieldListFilter

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'role', 'first_name', 'last_name')
    list_filter = ('role', 'email')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname')
    list_filter = ('surname',)

    fieldsets = (
        ('Author information', {
            'fields': ('name', 'surname', 'patronymic')
        }),
    )

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_authors')
    list_filter = ('id', 'name', ('authors', admin.RelatedOnlyFieldListFilter))

    def get_authors(self, obj):
        return ", ".join([str(author) for author in obj.authors.all()])
    get_authors.short_description = 'Authors'

    fieldsets = (
        ('Immutable data', {
            'fields': ('name', 'authors')
        }),
        ('Variable data', {
            'fields': ('count',)
        }),
    )

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_book_name', 'get_user_surname', 'created_at', 'end_at', 'plated_end_at')
    readonly_fields = ('id', 'user', 'book', 'created_at', 'end_at', 'plated_end_at')
    list_filter = (
        ('book', RelatedOnlyFieldListFilter),
        ('user', RelatedOnlyFieldListFilter),
        'end_at',
        'plated_end_at',
    )

    def get_book_name(self, obj):
        return obj.book.name
    get_book_name.short_description = 'Book'

    def get_user_surname(self, obj):
        return obj.user.last_name
    get_user_surname.short_description = 'User'
