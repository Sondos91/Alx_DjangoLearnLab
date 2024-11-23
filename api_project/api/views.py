from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.authtoken.views import Obtain_Auth_Token
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ObtainAuthTokenView(Obtain_Auth_Token):
    
    pass

class BookViewSet(viewsets.ModelViewSet):
    # ...
    permission_classes = [IsAuthenticated]
    # ...