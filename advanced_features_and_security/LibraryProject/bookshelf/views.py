from django.shortcuts import render, HttpResponse
from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from .models import Author, Book, Library, Librarian
from django.views.generic.detail import DetailView
from .models import Library
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse_lazy, path
from django.views.generic import CreateView
from django.contrib.auth import login
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import user_passes_test, login_required
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import user_passes_test
from .models import Bookshelf, Book
from .forms import ExampleForm



def home(request):
    return HttpResponse("Welcome to my Book Shelf.")




def list_books(request):
    """Retrieves all books renders a list of book titles and their authors."""
    books = Book.objects.all()      #fetch all book instances from the database
    context = {'list_books': books} #creates a context for the template
    return render(request, "relationship_app/list_books.html", context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = 'library'


    
#Register views using Django's built-in Usercreationform
class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

@login_required(login_url='relationship_app/login.html')
@login_required('login')
def role_view(request):
    return render(request, 'relationship_app/login.html')
                  
    # success_url = reverse_lazy('login')
    # template_name = 'relationship_app/login.html'




def role_required(role):
    def decorator(view_func):
        return user_passes_test(lambda u: u.userprofile.role == role)(view_func)
    return decorator


from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required(login_url='relationship_app/login.html')
@role_required('Admin')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required(login_url='relationship_app/login.html')
@role_required('Librarian')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required(login_url='relationship_app/login.html')
@role_required('Member')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        if title and author:
            book = Book(
                title=title,
                author=author
            )

            book.save()
            return redirect('book_list')
        
        else:
            return HttpResponse("All fields are required.", status=404)
    return render(request, 'relationship_app/add_book.html')

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        book.title = request.POST.get('title', book.title)
        book.author = request.POST.get('author', book.author)

        book.save()
        return render(request, 'relationship_app/edit_book.html', {'book': book})
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'relationship_app/delete_book.html', {'book': book})


@permission_required('Bookshelf.can_add', raise_exception=True)
def Bookshelf_detail(request, pk):
    Bookshelf = get_object_or_404(Bookshelf, pk=pk)
    return render(request, 'Bookshelf_detail')

@permission_required('Bookshelf.can_create', raise_exception=True)
def create_Bookshelf(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Bookshelf = Bookshelf.objects.create(title=title, content=content)
        return redirect('Bookshelf_details')
@permission_required('Bookshelf.can_edit', raise_exception=True)
def edit_Bookshelf(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Bookshelf = Bookshelf.objects.add(title=title, content=content)
        return redirect('Bookshelf_details')

def search_books(request):
    form = ExampleForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        books = Book.objects.filter(title__icontains=query)
    return render(request, 'bookshelf/book_list.html', {'form': form, 'books': books})
