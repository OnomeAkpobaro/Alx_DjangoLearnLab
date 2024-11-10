from multiprocessing import context
from django.shortcuts import render, redirect
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

#Fuction to check roles
def role_required(role):
    def decorator(view_func):
        return user_passes_test(lambda u: u.userprofile.role == role)(view_func)
    return decorator

#Admin view - accissible to users with Admin role
@login_required
@role_required('Admin')
def admin_view(request):
    return user_passes_test(request,'admin_view.html')
    # return render(request, 'admin_view.html')

#Librarian View - accessible to users with librarian role
@login_required
@role_required('Librarian')
def librarian_view(request):
    return user_passes_test(request, 'librarian_view.html')
    # return render(request, 'librarian_view.html')

#Member role - accessible to users with member role
@login_required
@role_required('Member')
def member_view(request):
    return user_passes_test(request, 'member_view.html')
    # return render(request, 'member_view.html')

