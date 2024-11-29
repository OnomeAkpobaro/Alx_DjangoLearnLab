from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'), #list all books
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'), #retrieve book by id
    path('books/create/', BookCreateView.as_view(), name='book-create'), #create a book
    path('books/update/', BookUpdateView.as_view(), name='book-update'), #update a book
    path('books/delete/', BookDeleteView.as_view(), name='book-delete'), #delete a book
]

