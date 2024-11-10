from multiprocessing import context
from django.shortcuts import render
from .models import Author, Book, Library, Librarian
from django.views.generic import DetailView
from .models import Library


# Create your views here.

def list_books(request):
    """Retrieves all books renders a list of book titles and their authors."""
    books = Book.objects.all()      #fetch all book instances from the database
    context = {'list_books': books} #creates a context dictionary with list of books
    return render(request, "relationship_app/list_books.html", context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        return context
    
    