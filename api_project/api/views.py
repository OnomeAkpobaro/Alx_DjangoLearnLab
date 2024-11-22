from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
# from django.views.decorators.csrf import csrf_exempt
# from django.http import HttpResponse, JsonResponse
# from rest_framework.parsers import JSONParser


# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()       #Fetches all book objects
    serializer_class = BookSerializer   #use the Bookserializer to serialize the queryset

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()        #Queryset to retrieve all books
    serializer_class =  BookSerializer  #Uses Bookserializer to serialize the data
    permission_classes = [IsAuthenticated]  #restricts all actions to authenticated users
# @csrf_exempt
# def BookList(request):
#     """
#     List all Books, or Create a new Book
#     """
#     if request.method == 'GET':
#         Book = Book.objects.all()
#         serializer = BookSerializer(Book, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = BookSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
    
# @csrf_exempt
# def BookViewSet(request, pk):
#     """
#     Retrieve, update or delete a book
#     """
#     try:
#         Book = Book.objects.get(pk=pk)
#     except Book.DoesNotExist:
#         return HttpResponse(status=404)
#     if request.method == 'GET':
#         serializer = BookSerializer(Book)
#         return JsonResponse(serializer.data)
    
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = BookSerializer(Book, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#     elif request.method =='DELETE':
#         Book.delete()
#         return HttpResponse(status=204)
    

    
