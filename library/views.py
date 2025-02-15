from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from library.models import Book, Author, BookIssue
from library.serializers import (
    BookSerializer,
    AuthorSerializer,
    BookIssueSerializer,
)
from users.permissions import IsModer, IsOwner
from library.pagination import CustomPagination


class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet для управления книгами.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "author__name", "genre"]
    ordering_fields = ["title", "published_year"]

    def perform_create(self, serializer):
        """
        Переопределение метода для добавления владельца книги.
        """
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        """
        Переопределение метода для назначения прав доступа.
        """
        if self.action == "create":
            self.permission_classes = [IsAuthenticated]
        elif self.action in ["update", "retrieve"]:
            self.permission_classes = [IsAuthenticated, IsModer | IsOwner]
        elif self.action == "destroy":
            self.permission_classes = [IsAuthenticated, IsOwner]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()


class AuthorViewSet(viewsets.ModelViewSet):
    """
    ViewSet для управления авторами.
    """

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name"]
    ordering_fields = ["name"]


class BookIssueViewSet(viewsets.ModelViewSet):
    """
    ViewSet для управления выдачей книг.
    """

    queryset = BookIssue.objects.all()
    serializer_class = BookIssueSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["book__title", "user__username"]
    ordering_fields = ["issue_date", "return_date"]

    def perform_create(self, serializer):
        """
        Переопределение метода для добавления информации о пользователе.
        """
        serializer.save(user=self.request.user)

    def get_permissions(self):
        """
        Переопределение метода для назначения прав доступа.
        """
        if self.action == "create":
            self.permission_classes = [IsAuthenticated]
        elif self.action in ["update", "retrieve"]:
            self.permission_classes = [IsAuthenticated, IsOwner]
        elif self.action == "destroy":
            self.permission_classes = [IsAuthenticated, IsOwner]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()
