from django.urls import path
from . import views
from django.views.generic import TemplateView
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, add_comment, CommentDeleteView, CommentUpdateView, search_posts, posts_by_tag

urlpatterns = [
    path('', TemplateView.as_view(template_name='blog/base.html'), name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('posts/<int:post_id>/comments/new/', add_comment, name='add_comment'),
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-edit'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='coment-delete'),
    path('search/', search_posts, name='search'),
    path('tags/<slug:tag_slug>/', posts_by_tag, name='posts-by-tag'),
]