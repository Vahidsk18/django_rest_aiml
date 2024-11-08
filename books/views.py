from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
class BookListCreate(generics.ListCreateAPIView):
    queryset =Book.objects.all()
    serializer_class=BookSerializer
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset =Book.objects.all()
    serializer_class=BookSerializer