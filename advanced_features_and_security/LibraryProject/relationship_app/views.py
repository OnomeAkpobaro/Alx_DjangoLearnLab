from django.shortcuts import render
from .models import Author, Book, Library, Librarian
from django.shortcuts import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to my Book Shelf.")

def list_books(request):
    """Retrieves all books renders a list of book titles and their authors."""
    books = Book.objects.all()      #fetch all book instances from the database
    context = {'list_books': books} #creates a context dictionary with book list 
    return render(request, 'books/list_books.html', context)

from django.views.generic import DetailView
from .models import Library


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'Library_detail.html'
    context_object_name = 'library'

    