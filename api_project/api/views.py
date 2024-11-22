from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()       #Fetches all book objects
    serializer_class = BookSerializer   #use the Bookserializer to serialize the queryset