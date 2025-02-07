from django.urls import path
from .views import (
    AuthorListCreateView,
    AuthorRetrieveUpdateDeleteView,
    BookListCreateView,
    BookRetrieveUpdateDeleteView,
)

urlpatterns = [
    # Author endpoints
    path('authors/', AuthorListCreateView.as_view(), name='author-list-create'),
    path('authors/<str:pk>/', AuthorRetrieveUpdateDeleteView.as_view(), name='author-detail'),

    # Book endpoints
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<str:pk>/', BookRetrieveUpdateDeleteView.as_view(), name='book-detail'),
]
