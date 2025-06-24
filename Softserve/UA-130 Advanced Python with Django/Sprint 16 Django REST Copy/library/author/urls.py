from django.urls import path
from . import views

urlpatterns = [
    path('', views.author_list_view, name='author_list'),
    path('create/', views.create_author_view, name='create_author'),
    path('delete/<int:author_id>/', views.delete_author_view, name='delete_author'),
]