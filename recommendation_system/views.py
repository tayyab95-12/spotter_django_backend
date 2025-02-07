from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q

from django_backend import settings
from .models import FavoriteBooks
from library.models import Book
from library.serializers import BookSerializer
from .serializers import FavoriteBookSerializer
from .utils import get_recommendations


class FavoritesView(APIView):
    """
    API for managing user favorites and suggesting books.
    Supports:
    - POST: Add a book to favorites
    - DELETE: Remove a book from favorites
    - GET: Fetch the user's favorite books and recommended books
    """

    def get(self, request):
        """
        Fetch the user's favorite books and recommendations.
        """
        user = request.user
        favorite_books, created = FavoriteBooks.objects.get_or_create(user=user)

        # Serialize favorites
        favorite_books_list = favorite_books.books.all()
        favorites_serialized = BookSerializer(favorite_books_list, many=True).data

        # Generate recommendations based on favorite books
        if favorite_books_list.exists():
            recommendations = get_recommendations(favorite_books_list)
            recommendations_serialized = BookSerializer(recommendations, many=True).data
        else:
            recommendations_serialized = []

        return Response({
            "favorites": favorites_serialized,
            "recommendations": recommendations_serialized
        }, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Add a book to the user's favorites.
        """
        serializer = FavoriteBookSerializer(data=request.data)  # Validate input with serializer

        if serializer.is_valid():

            favorite_books, created = FavoriteBooks.objects.get_or_create(user=self.request.user)

            # Fetch the book
            try:
                book = Book.objects.get(id=serializer.validated_data['book_id'])
            except Book.DoesNotExist:
                return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

            # Check if max favorites limit is reached
            if favorite_books.books.count() >= settings.MAX_FAVORITES:
                return Response({"error": f"You can only have up to {settings.MAX_FAVORITES} favorite books."},
                                status=status.HTTP_400_BAD_REQUEST)

            # Add book to favorites
            favorite_books.books.add(book)
            return Response({"message": "Book added to favorites"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        """
        Remove a book from the user's favorites.
        """
        user = request.user
        book_id = request.data.get("book_id")
        if not book_id:
            return Response({"error": "Book ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        favorite_books, created = FavoriteBooks.objects.get_or_create(user=user)

        # Fetch the book
        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

        # Remove book from favorites
        favorite_books.books.remove(book)
        return Response({"message": "Book removed from favorites"}, status=status.HTTP_200_OK)
