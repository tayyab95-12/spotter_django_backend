
from django.contrib.auth.models import User  # Assuming you're using Django's default User model
from django.db import models


class FavoriteBooks(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="favorite_books")
    books = models.ManyToManyField('library.Book', related_name="favorited_by")

    def __str__(self):
        return f"{self.user}'s favorite books"
