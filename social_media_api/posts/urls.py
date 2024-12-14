from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, UserFeedView, UnlikePostView, LikePostView 
from django.urls import path

router = DefaultRouter()

router.register('posts', PostViewSet)

router.register('comments', CommentViewSet)

urlpatterns = [
    path('feed/', UserFeedView.as_view(), name='user-feed'),
    path('<int:pk>/like/', LikePostView.as_view(), name='like-post'),
    path('<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'),
    
]
urlpatterns += router.urls