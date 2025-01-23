from rest_framework import serializers
from .models import Book, Author, BookIssue


class BookSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Book.
    """

    class Meta:
        model = Book
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Author.
    """

    class Meta:
        model = Author
        fields = "__all__"


class BookIssueSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели BookIssue.
    """

    class Meta:
        model = BookIssue
        fields = "__all__"
