from django.urls import path
from . import views
from .views import create_book

urlpatterns = [
    path('user/', views.book_list_view, name='user_book_list'),
    path('user/<int:book_id>/', views.book_detail_view, name='user_book_detail'),
    path('librarian/', views.book_list_view, name='librarian_book_list'),
    path('librarian/<int:book_id>/', views.book_detail_view, name='librarian_book_detail'),
    path('create/', views.create_book_view, name='create_book'),
    path('update/<int:book_id>/', views.update_book_view, name='update_book'),
    path('delete/<int:book_id>/', views.delete_book_view, name='delete_book'),
    path('provided/<int:user_id>/', views.user_books_view, name='user_books'),
    path('add/', create_book, name='create_book'),
]
