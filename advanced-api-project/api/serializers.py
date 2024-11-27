from rest_framework import serializers
from .models import Author, Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model
    """
    class Meta:
        model = 'Book'
        fields = ("id", "title", "publication_year", "author")

    def validate_publication_year(self, value):
        if value > date.today().year:
            raise serializers.ValidationError("Publication year can't be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author, inluding a nested bookserializer to serialize related books.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = 'Author'
        fields = ("id", "name", "books")
