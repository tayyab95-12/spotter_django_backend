from rest_framework import serializers
from .models import Author, Book


# Serializer for the Author model
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"
        read_only_fields = ['id']


# Serializer for the Book model
class BookSerializer(serializers.ModelSerializer):
    authors = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Author.objects.all(), required=False
    )

    class Meta:
        model = Book
        fields = "__all__"
        read_only_fields = ['id']

    # Override `to_representation` for detailed author serialization when fetching
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Replace authors with nested serialized author data
        representation['authors'] = AuthorSerializer(instance.authors.all(), many=True).data
        return representation


