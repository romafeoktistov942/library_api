from django.db import models
from django.conf import settings


class Book(models.Model):
    """
    Модель для представления книги в библиотеке.
    """

    title = models.CharField(
        max_length=255,
        verbose_name="Название книги",
        help_text="Введите название книги",
    )
    author = models.ForeignKey(
        "Author",
        on_delete=models.CASCADE,
        verbose_name="Автор",
        help_text="Выберите автора книги",
    )
    genre = models.CharField(
        max_length=100,
        verbose_name="Жанр книги",
        help_text="Введите жанр книги",
    )
    publication_year = models.PositiveIntegerField(
        verbose_name="Год издания",
        help_text="Введите год издания книги",
    )
    copies_count = models.PositiveIntegerField(
        verbose_name="Количество экземпляров",
        help_text="Введите количество экземпляров книги",
        default=1,
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата обновления"
    )

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.title


class Author(models.Model):
    """
    Модель для представления автора книги.
    """

    name = models.CharField(
        max_length=255,
        verbose_name="Имя автора",
        help_text="Введите имя автора",
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата обновления"
    )

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    def __str__(self):
        return self.name


class BookIssue(models.Model):
    """
    Модель для представления выдачи книги пользователю.
    """

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        verbose_name="Книга",
        help_text="Выберите книгу, которую выдают",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        help_text="Выберите пользователя, которому выдают книгу",
    )
    issue_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата выдачи",
        help_text="Дата, когда книга была выдана",
    )
    return_date = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Дата возврата",
        help_text="Дата, когда книга была возвращена",
    )
    is_returned = models.BooleanField(
        default=False,
        verbose_name="Возвращена",
        help_text="Статус возврата книги",
    )

    class Meta:
        verbose_name = "Выдача книги"
        verbose_name_plural = "Выдачи книг"

    def __str__(self):
        return f"{self.book.title} выдана {self.user.username}"
