from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, UserFeedView
from django.urls import path

router = DefaultRouter()

router.register('posts', PostViewSet)

router.register('comments', CommentViewSet)

urlpatterns = [
    path('feed/', UserFeedView.as_view(), name='user-feed'),
]
urlpatterns += router.urls