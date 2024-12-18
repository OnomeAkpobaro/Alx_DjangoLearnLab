from django.urls import path, include
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')
urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),   #Map to the BookList view
    # path('Books/<int:pk>/'),
    path('', include(router.urls)), #This includes al routes registered with the router
]

urlpatterns = [
    path('auth/token/', obtain_auth_token, name='get-token'),

]