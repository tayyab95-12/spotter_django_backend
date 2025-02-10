from rest_framework import generics, filters
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


# Author API Views
class AuthorListCreateView(generics.ListCreateAPIView):
    """
    GET: List all authors
    POST: Create a new author
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve details of a specific author
    PUT: Update a specific author
    DELETE: Delete a specific author
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookListCreateView(generics.ListCreateAPIView):
    """
    GET: List all books
    POST: Create a new book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', "authors__name"]



class BookRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve details of a specific book
    PUT: Update a specific book
    DELETE: Delete a specific book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
