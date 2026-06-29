from django.urls import path
from .views import home, category_books, book_create, book_update, book_delete

urlpatterns = [
    path('', home, name='home'),
    path('create/', book_create, name='book_create'),
    path('update/<int:pk>/', book_update, name='book_update'),
    path('delete/<int:pk>/', book_delete, name='book_delete'),
    path('category/<int:id>/', category_books, name='category_books'),
]