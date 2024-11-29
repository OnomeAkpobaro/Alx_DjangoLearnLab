from rest_framework import generics, permissions
from .serializers import AuthorSerializer, BookSerializer
from .models import Book
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, BasePermission
# Create your views here.

#Listview - To retrieve all books
class BookListView(generics.ListAPIView):
    queryset= Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = []         #Open for everyone to read

    def perform_create(self, serializer):
        serializer.save()

#Detailview - To retrieve a singe book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'
    permission_classes = []         #Open for everyone to read

#Createview - To add a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]      #Only authenticated users can creeate a book
#Updateview - To modify an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]      #Only authenticated users can update a book
#Deleteview - To remove a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]      #Only authenticated users can delete a book

class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow authenticated users to edit
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        #write permissions are only allowed to authenticated users
        return request.user