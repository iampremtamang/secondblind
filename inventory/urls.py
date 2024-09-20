from django.urls import path

from .views import book_list, book_create, export_books


urlpatterns = [
    path('', book_list, name='book_list'),
    path('create/', book_create, name='book_create'),
    path('export/', export_books, name='export_books'),
]
