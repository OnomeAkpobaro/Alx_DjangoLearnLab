from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
# from django.urls import path

router = DefaultRouter()

router.register('posts', PostViewSet)

router.register('comments', CommentViewSet)

# urlpatterns = [
#     path('auth/', )
# ]
urlpatterns = router.urls