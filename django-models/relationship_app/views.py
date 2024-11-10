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
    
#Register views using Django's built-in Usercreationform
class RegisterView(CreateView):
    form_class = UserCreationForm()
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

class RoleView():
    form_class = login_required()
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/login.html'

# Fuction to check roles
# def role_required(role):
#     def decorator(view_func):
#         return user_passes_test(lambda u: u.userprofile.role == role)(view_func)
#     return decorator

# #Admin view - accissible to users with Admin role
# @login_required(login_url='admin_views.html')
# # @role_required('Admin')
# @user_passes_test(admin_view)
# def admin_view(request):
#     return render(request, 'admin_view.html')

# #Librarian View - accessible to users with librarian role
# @login_required(login_url='librarian_view.html')
# # @role_required('Librarian')
# @user_passes_test(librarian_view)
# def librarian_view(request):
#     return render(request, 'librarian_view.html')

# #Member role - accessible to users with member role
# @login_required
# @role_required('Member')
# def member_view(request):
#     return user_passes_test(request, 'member_view.html')
#     # return render(request, 'member_view.html')

from django.contrib.auth.decorators import user_passes_test

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
    return render(request, 'add_book.html')

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'delete_book.html', {'book': book})

