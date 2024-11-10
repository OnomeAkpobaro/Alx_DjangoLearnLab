from django.urls import path
from . import views
from .views import list_books
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse_lazy, path
from django.views.generic import CreateView


urlpatterns = [
    path('books/', views.list_books, name='list_books'),        #URL for listing all books
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),      #URL for library details

]

urlpatterns =[
    path('login/', views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),

    path('logout/', views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    path('register/', views.register, name='admin_view'),

    path('librarian/', views.librarian_view, name='librarian_view'),

    path('member/', views.member_view, name='member_view'),



    path('add/', views.add_book, name='add_book'),
    path('edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
]