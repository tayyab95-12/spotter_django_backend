from django.db import models



class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)  # Name of the author
    gender = models.CharField(max_length=50, blank=True, null=True)  # Gender (optional)
    image_url = models.URLField(max_length=500, blank=True, null=True)  # URL of the author's image
    about = models.TextField(blank=True, null=True)  # Description or biography of the author
    fans_count = models.PositiveIntegerField(default=0)  # Number of fans
    average_rating = models.FloatField(blank=True, null=True)  # Average rating by readers
    ratings_count = models.PositiveIntegerField(default=0)  # Total number of ratings
    text_reviews_count = models.PositiveIntegerField(default=0)  # Total number of text reviews
    works_count = models.PositiveIntegerField(default=0)  # Number of works authored or associated with

    def __str__(self):
        return self.name

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    language = models.CharField(max_length=50, blank=True, null=True)
    isbn = models.CharField(max_length=13, blank=True, null=True)
    isbn13 = models.CharField(max_length=13, blank=True, null=True)
    asin = models.CharField(max_length=10, blank=True, null=True)
    average_rating = models.FloatField(blank=True, null=True)
    ratings_count = models.PositiveIntegerField(blank=True, null=True)
    text_reviews_count = models.PositiveIntegerField(blank=True, null=True)
    publication_date = models.DateField(blank=True, null=True)
    original_publication_date = models.DateField(blank=True, null=True)
    format = models.CharField(max_length=50, blank=True, null=True)
    edition_information = models.CharField(max_length=255, blank=True, null=True)
    image_url = models.URLField(max_length=500, blank=True, null=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    num_pages = models.PositiveIntegerField(blank=True, null=True)
    series_id = models.CharField(max_length=255, blank=True, null=True)
    series_name = models.CharField(max_length=255, blank=True, null=True)
    series_position = models.CharField(max_length=50, blank=True, null=True)
    authors = models.ManyToManyField(Author, related_name="books", blank=True)

    def __str__(self):
        return self.title
