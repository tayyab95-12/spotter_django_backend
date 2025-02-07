from rest_framework import serializers


class FavoriteBookSerializer(serializers.Serializer):
    book_id = serializers.IntegerField(required=True)

