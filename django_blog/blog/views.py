from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid Credentials.'})
    else:
        return render(request, 'login.html')
    

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def profile(request):
    if request.method == 'POST':
        user = request.user
        user.email = request.POST.get('email', user.email)
        user.save()
        return HttpResponseRedirect('/profile')
    return render(request, 'profile.html', {'user': request.user})
#Listview to display all blog posts
class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    paginate_by = 5
#Detailview to display a single post
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'posts'
#Createview for authenticated users
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'post_form.html'
    fields = ['title', 'content']

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post-list')

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author