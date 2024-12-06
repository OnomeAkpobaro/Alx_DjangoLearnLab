from django.urls import path
from . import views
from django.views.generic import TemplateView
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html'), name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]